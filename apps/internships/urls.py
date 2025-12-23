from django.urls import path
from .views import (PracticaListView, PracticaApproveAcademicView, PracticaActivateView)

urlpatterns = [
    path("practicas/", PracticaListView.as_view()),
    path("practicas/<int:pk>/habilitar-academicamente/", PracticaApproveAcademicView.as_view()),
    path("practicas/<int:pk>/activar/", PracticaActivateView.as_view()),
]