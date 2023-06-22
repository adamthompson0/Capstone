from django.shortcuts import render, get_object_or_404
import requests
# Create your views here.
def index(request):
    return render(request, 'weather/index.html')
