from django.shortcuts import render
import requests
from .keys import api
from weather.models import Location, Weather, Forecast, Subscription

# Create your views here.

def weather(request):
    location = 'Beaverton,OR,USA'
    start_date = '2023-06-23'
    end_date = '2023-06-24'
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{start_date}/{end_date}/?unitGroup=us&key={api}'
    response = requests.get(url).json()

    weather = {
        'location': location,
        'temperature': response['days'][0]['temp'],
        'description': response['days'][0]['conditions'],
        'icon': response['days'][0]['icon'],
    }

    context = {
        'weather': weather
    }
    print(weather)
    return render(request,'weather/index.html', context)
    
