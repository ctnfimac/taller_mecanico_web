from django.contrib.auth.models import Group, User
from apps.cars.models import Car
from rest_framework import serializers


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'licence_plate', 'year',
                  'email', 'kilometers']