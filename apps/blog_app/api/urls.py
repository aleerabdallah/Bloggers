from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter



# router = DefaultRouter()

# router.register('posts', views.PostAPIView, basename="posts")

# blogurl_patterns = router.urls


blogurl_patterns = [
    path("posts/", views.PostsAPIView.as_view(), name="posts"),
    path("posts/<int:pk>/", views.PostAPIView.as_view(), name="posts"),
    
]