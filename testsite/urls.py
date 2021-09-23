from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('testsite.apps.public.urls')),
    path("accounts/", include('testsite.apps.accounts.urls')),
]
