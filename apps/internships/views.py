from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from .models import Practica
from .serializers import PracticaSerializer

class PracticaListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        internships = Practica.objects.all()
        serializer = PracticaSerializer(internships, many=True)
        return Response(serializer.data)
    
class PracticaApproveAcademicView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        internship = get_object_or_404(Practica, pk=pk)

        try:
            internship.approve_academically(tutor=request.user.tutor)
        except ValidationError as e:
            return Response({"detail": e.message}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"message": "Práctica habilitada académicamente"}, status=status.HTTP_200_OK)
    
class PracticaActivateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        internship = get_object_or_404(Practica, pk=pk)

        try:
            internship.activate()
        except ValidationError as e:
            return Response({"detail": e.message}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"message": "Práctica activada!"}, status=status.HTTP_200_OK)