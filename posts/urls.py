from django.urls import path, re_path

from posts.views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView

app_name = "posts"

urlpatterns = [
    path('ListCreate', PostListCreateAPIView.as_view(), name='list_create'),
    re_path(r'^RetrieveUpdateDestroy/(?P<pk>\d+)$', PostRetrieveUpdateDestroyAPIView.as_view(),
            name='retrieve_update_destroy')
]
