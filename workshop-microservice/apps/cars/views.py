from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.cars.models import Car, WorkshopCar
from apps.cars.serializers.workshop_serializers import CarSerializer, WorkshopCarSerializer
from apps.cars.serializers.car_serializers import SearchCarSerializer
from utils.auth import get_payload_from_token, validate_token
from rest_framework.decorators import action

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



class CarByLicencePlateView(viewsets.ModelViewSet):
    """API Endpoint para la busqueda de autos
    por los parámetros que vaya definiendo 
    """
    queryset = Car.objects.all()
    serializer_class = SearchCarSerializer

    @action(detail=False, methods=['get'], url_path='car')
    def by_licence(self, request, licence_plate=None):
        
        licence_plate = request.query_params.get('licence_plate')
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

        try:
            car = Car.objects.get(licence_plate__iexact=licence_plate)
        except Car.DoesNotExist:
            return Response({"error": "Auto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        if not WorkshopCar.objects.filter(workshop=workshop_id, car=car).exists():
            return Response({"error": "El auto no pertenece al taller del usuario"}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(car)
        return Response(serializer.data)
        