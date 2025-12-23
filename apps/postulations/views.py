from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from .models import Postulacion
from .serializers import PostulacionCreateSerializer, PostulacionListSerializer

class PostulacionListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        postulations = Postulacion.objects.all()
        serializer = PostulacionListSerializer(postulations, many=True)
        return Response(serializer.data)

class PostulacionCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PostulacionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            Postulacion.objects.create(estudiante=request.user.estudiante, oferta=serializer.validated_data["oferta"])
        except IntegrityError:
            raise ValidationError({"detail": "Ya aplicaste a esta oferta."})

        return Response({"message": "Postulación realizada correctamente!"}, status=status.HTTP_201_CREATED)

class PostulacionAcceptView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        postulation = get_object_or_404(Postulacion, pk=pk)

        try:
            postulation.accept(accepted_by_user=request.user)
        except ValidationError as e:
            return Response({"detail": e.message}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"message": "Postulación aceptada!"}, status=status.HTTP_200_OK)