from django.contrib import admin
from .models import Location, Forecast, Weather, Subscription

# Register your models here.
admin.site.register(Location)
admin.site.register(Forecast)
admin.site.register(Weather)
admin.site.register(Subscription)