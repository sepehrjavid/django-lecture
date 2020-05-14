from django.urls import path

from posts.views import PostCreateAPIView

urlpatterns = [
    path('create', PostCreateAPIView.as_view())
]
