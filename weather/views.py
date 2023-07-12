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
            'sunset': response['currentConditions']['sunset'],
            'sunrise': response['currentConditions']['sunrise']

        }

        context = {
            'weather': weather
        }
        return render(request,'weather/detail.html', context)
    else:
        return render(request,'weather/home.html')
    

def compare(request):
    if request.method == 'POST':
        location1 = request.POST['location1']
        location2 = request.POST['location2']
        url1 = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location1}/?unitGroup=us&key={api}'
        url2 = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location2}/?unitGroup=us&key={api}'
        response1 = requests.get(url1).json()
        response2 = requests.get(url2).json()

        weather = {
            'location1': location1,
            'location2': location2,
            'time_zone1': response1['timezone'],
            'time_zone2': response2['timezone'],
            'date1': response1['currentConditions']['datetime'],
            'date2': response2['currentConditions']['datetime'],
            'temperature1': response1['currentConditions']['temp'],
            'temperature2': response2['currentConditions']['temp'],
            'tempmax1': response1['days'][0]['tempmax'],
            'tempmax2': response2['days'][0]['tempmax'],
            'tempmin1': response1['days'][0]['tempmin'],
            'tempmin2': response2['days'][0]['tempmin'],
            'description1': response1['days'][0]['conditions'],
            'description2': response2['days'][0]['conditions'],
            'icon1': response1['days'][0]['icon'],
            'icon2': response2['days'][0]['icon'],
            'longitude1': response1['longitude'],
            'longitude2': response2['longitude'],
            'latitude1': response1['latitude'],
            'latitude2': response2['latitude'],
            'uvindex1': response1['currentConditions']['uvindex'],
            'uvindex2': response2['currentConditions']['uvindex'],
            'sunset1': response1['currentConditions']['sunset'],
            'sunset2': response2['currentConditions']['sunset'],
            'sunrise1': response1['currentConditions']['sunrise'],
            'sunrise2': response2['currentConditions']['sunrise']
        }
        context = {
            'weather': weather
        }
        return render(request,'weather/compare.html', context)
    else:
        return render(request,'weather/compare.html')
    