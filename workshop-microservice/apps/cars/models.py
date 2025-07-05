from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    licence_plate = models.CharField(max_length=10, unique=True)
    year = models.CharField(max_length=4)
    email = models.EmailField(max_length=30, unique=True)
    kilometers = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "car"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.licence_plate})"
    
    
class WorkshopCar(models.Model):
    workshop = models.IntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('workshop', 'car')
        db_table = "workshop_car"

    def __str__(self):
        return f"{self.workshop} - {self.car}"