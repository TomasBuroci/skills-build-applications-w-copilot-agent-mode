"""
octofit_tracker URL Configuration

All REST API endpoints are available at:
    https://$CODESPACE_NAME-8000.app.github.dev/api/[component]/
or
    http://localhost:8000/api/[component]/
where $CODESPACE_NAME is taken from the environment variable.
"""
import os
from django.contrib import admin
from django.urls import path, include
from .views import api_root, router

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
    path('', api_root),
]
