from django.urls import path
from .views import (PostulacionCreateView, PostulacionAcceptView, PostulacionListView)

urlpatterns = [
    path("postulaciones/", PostulacionListView.as_view()),
    path("postulaciones/", PostulacionCreateView.as_view(), name="postulacion-create"),
    path("postulaciones/<int:pk>/aceptar/", PostulacionAcceptView.as_view()),
]