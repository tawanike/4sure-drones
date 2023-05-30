from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/drones", include("drones.urls")),
    path("v1/medication", include("medication.urls")),
]
