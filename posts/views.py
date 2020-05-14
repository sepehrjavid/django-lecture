from rest_framework import status
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from posts.serializers import PostSerializer


class PostCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# class PostCreateAPIView(APIView):
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(author=request.user)
#         return Response(status=status.HTTP_201_CREATED)
