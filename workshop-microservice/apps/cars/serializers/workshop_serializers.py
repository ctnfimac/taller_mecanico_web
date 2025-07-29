from apps.cars.models import Car, WorkshopCar
from rest_framework import serializers


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'licence_plate', 'year',
                  'email', 'kilometers']
        

class WorkshopCarSerializer(serializers.HyperlinkedModelSerializer):
    car = CarSerializer() 

    class Meta:
        model = WorkshopCar
        fields = ['car', 'created_at', 'workshop']