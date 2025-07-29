from apps.cars.models import Car
from rest_framework import serializers


# PARA LOS BUSCADORES
class SearchCarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'licence_plate', 'year',
                  'email', 'kilometers', 'created_at','updated_at']