from django.db import models

class Status(models.Model):
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "status"

    def __str__(self):
        return self.description



class Job(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    kilometer = models.IntegerField()
    service_date = models.DateTimeField()
    workshop_id = models.IntegerField()
    status_id = models.IntegerField()
    car_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "job"

    def __str__(self):
        return f"Job #{self.id} - {self.car}"


class Detail(models.Model):
    description = models.CharField(max_length=255)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='details')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "detail"

    def __str__(self):
        return self.description