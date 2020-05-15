from django.urls import path, re_path

from posts.views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView, RateAPIView

urlpatterns = [
    path('list_create', PostListCreateAPIView.as_view()),
    re_path(r'^retrieve_update_destroy/(?P<pk>\d+)$', PostRetrieveUpdateDestroyAPIView.as_view()),
    re_path(r'^rate/(?P<pk>\d+)$', RateAPIView.as_view())
]
