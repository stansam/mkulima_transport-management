from django.db import models
from django.utils import timezone

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20, unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return self.vehicle_number

class Driver(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    license_number = models.CharField(max_length=20, unique=True)
    assigned_vehicle = models.OneToOneField('Vehicle', on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_driver')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Job(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='jobs')
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='jobs')
    pickup_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    scheduled_date = models.DateField()
    scheduled_time = models.TimeField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Job for {self.farmer} with {self.vehicle} by {self.driver} at {self.created_at}"
    


class Revenue(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='revenues')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Revenue for Job {self.job.id}: {self.amount}"