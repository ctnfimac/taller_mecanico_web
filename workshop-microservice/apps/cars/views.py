from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.cars.models import Car, WorkshopCar
from apps.cars.serializers import CarSerializer, WorkshopCarSerializer
from utils.auth import get_payload_from_token, validate_token
import requests

class CarViewSet(viewsets.ModelViewSet):
    """
    API endpoint para obtener todos los autos registrados
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
    def list(self, request, *args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return Response(
                {"detail": "Token no proporcionado"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        token = token.strip()
        # Verifico el token 
        valid, data = validate_token(token)
        if not valid:
            return Response(
                    {"detail": data.get("message", "Problemas en el sistema")}, 
                    status=data.get("status_code")
                )
        
        return super().list(request, *args, **kwargs)
    

class WorkshopCarViewSet(viewsets.ModelViewSet):
    """
    API endpoint para obtener todos los autos registrados
    de un Workshop determinado
    """
    queryset = Car.objects.all()
    serializer_class = WorkshopCarSerializer

    def get_queryset(self):
        workshop_id = getattr(self.request, 'workshop_id', None)
        if not workshop_id:
            return WorkshopCar.objects.none()
        return WorkshopCar.objects.filter(workshop=workshop_id)

    
    def list(self, request, *args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return Response(
                {"detail": "Token no proporcionado"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        token = token.strip()
        valid, data = validate_token(token)
        if not valid:
            return Response(
                {"detail": data.get("message", "Problemas en el sistema")},
                status=data.get("status_code", status.HTTP_401_UNAUTHORIZED)
            )

        payload = get_payload_from_token(token)
        workshop_id = payload.get("workshop_id")
        # Guarda el workshop_id en el request para usarlo en get_queryset
        request.workshop_id = workshop_id

        return super().list(request, *args, **kwargs)
        