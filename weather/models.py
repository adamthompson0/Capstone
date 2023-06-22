from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.city}, {self.state}, {self.country}"
    
class Weather(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)
    precipitation = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f"{self.location}, {self.temperature}, {self.humidity}, {self.wind_speed}, {self.precipitation}"
    
class Forecast(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)
    precipitation = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f"{self.location}, {self.date}, {self.temperature}, {self.humidity}, {self.wind_speed}, {self.precipitation}"

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return self.user
    
