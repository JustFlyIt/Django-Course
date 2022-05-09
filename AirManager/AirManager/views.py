from django.http import HttpResponse
from django.shortcuts import render
from .models import Aircraft

def aircraft(request):
    aircraftData = Aircraft.objects.all()
    return render(request, 'aircraft/aircraftList.html', {'AircraftData': aircraftData})

def home(request):
    return HttpResponse("Home Page")
