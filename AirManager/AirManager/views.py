from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Aircraft

def aircraft(request):
    aircraftData = Aircraft.objects.all()
    return render(request, 'aircraft/aircraftList.html', {'aircraftData':aircraftData})

def home(request):
    return HttpResponse("Home Page")

def acDetail(request, id):
    aircraftData = Aircraft.objects.get(pk=id)
    return render(request, 'aircraft/acDetail.html', {'acDetail':aircraftData})

def addAC(request):
    name = request.POST.get('name')
    type = request.POST.get('type')

    if name and type:
            ac = Aircraft(name=name, type=type)
            ac.save()
            return HttpResponseRedirect('/aircraft')

    return render(request, 'aircraft/addAC.html')

def deleteAC(request, id):
    try:
        ac = Aircraft.objects.get(pk=id)
    except:
        raise Http404("AC does not exist....")

    ac.delete()

    return HttpResponseRedirect('/aircraft')
