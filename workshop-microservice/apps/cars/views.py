from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.cars.models import Car
from apps.cars.serializers import CarSerializer
from utils.auth import validate_token
import requests

class CarViewSet(viewsets.ModelViewSet):
    """
    API endpoint para obtener todos los autos registrados
    """
    queryset = Car.objects.all()#.order_by('-date_joined')
    serializer_class = CarSerializer

    def list(self, request, *args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return requests.Response({"detail": "Token no proporcionado"}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Si el token viene como "Bearer <token>", extrae solo el token
        # En mi caso no es necesario
        if token.startswith("Bearer "):
            token = token[7:]
        
        # Verifico el token 
        valid, data = validate_token(token)
        if not valid:
            return Response(
                    {"detail": data.get("message", "Problemas en el sistema")}, 
                    status=data.get("status_code")
                )
        
        return super().list(request, *args, **kwargs)