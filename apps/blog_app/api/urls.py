from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter



# router = DefaultRouter()

# router.register('posts', views.PostAPIView, basename="posts")

# blogurl_patterns = router.urls


blogurl_patterns = [
    path("posts/", views.PostsAPIView.as_view(), name="posts"),
    path("posts/<str:slug>/", views.PostAPIView.as_view(), name="posts"),
    path("category/<str:name>/", views.CategoryAPIView.as_view(), name="posts_by_cat"),
    path("tag/<str:name>/", views.TagAPIView.as_view(), name="posts_by_tag"),
    
]