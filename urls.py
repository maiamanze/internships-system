from django.urls import path, include

urlpatterns = [
    path("api/", include("apps.internships.urls")),
    path("api/", include("apps.postulations.urls")),
]
