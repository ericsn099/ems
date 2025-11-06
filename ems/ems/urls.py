from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("ems/", include("ems.urls")),
    path("admin/", admin.site.urls),
]