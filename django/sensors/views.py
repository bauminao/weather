from django.shortcuts import render

from django.http import HttpResponse

import requests

def index(request):
    return HttpResponse("Hello, world. You're at the sensors index.")

def sensor(request, sensorIP):
    response = requests.get('http://'+str(sensorIP)+':2905')
    return HttpResponse(response)

