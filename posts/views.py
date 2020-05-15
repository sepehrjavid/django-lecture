from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post, Rating
from posts.permissions import IsOwnerOrReadOnly, CanCreatePermission
from posts.serializers import PostSerializer, RatingSerializer


class PostListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, CanCreatePermission]
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        if self.request.GET.get('q'):
            return Post.objects.filter(
                Q(title__icontains=self.request.GET.get('q')) | Q(body__icontains=self.request.GET.get('q')))
        return Post.objects.all()


# class PostCreateAPIView(APIView):
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(author=request.user)
#         return Response(status=status.HTTP_201_CREATED)


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]


class RateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('pk'))
        serializer.save(user=self.request.user, post=post)
