from django.urls import path
from .api.urls import newsletter_pattern





app_name = "newsletter"

urlpatterns = [
] 

urlpatterns += newsletter_pattern

