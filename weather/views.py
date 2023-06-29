from django.shortcuts import render, get_object_or_404
import requests
from api.keys import api
# Create your views here.
def index(request):
    if request.method == 'POST':
        location = request.POST['location']
        url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/?unitGroup=us&key={api}'
        response = requests.get(url).json()

        weather = {
            'location': location,
            'time_zone': response['timezone'],
            'date': response['currentConditions']['datetime'],
            'temperature': response['currentConditions']['temp'],
            'tempmax': response['days'][0]['tempmax'],
            'tempmin': response['days'][0]['tempmin'],
            'description': response['days'][0]['conditions'],
            'icon': response['days'][0]['icon'],
            'longitude': response['longitude'],
            'latitude': response['latitude'],
            'uvindex': response['currentConditions']['uvindex'],

        }

        context = {
            'weather': weather
        }
        return render(request,'weather/index.html', context)
    else:
        return render(request,'weather/index.html')