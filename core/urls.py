"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static
from core.settings.common import DEBUG
from debug_toolbar.toolbar import debug_toolbar_urls




urlpatterns = [
    path('blogger/admin/', admin.site.urls),
    path('blog/', include('blog_app.urls')),
    path('newsletter/', include('newsletter.urls')),


    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Tinymce editor
    # path('tinymce/', include('tinymce.urls')),
]  

if DEBUG:
    urlpatterns = [
        *urlpatterns,
    ] + debug_toolbar_urls()


urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


# if DEBUG:
#     urlpatterns + debug_toolbar_urls()



