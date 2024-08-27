from django.urls import path
from . import views








blogurl_patterns = [
    path("posts/", views.PostAPIView.as_view(), name="posts"),
]