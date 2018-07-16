from django.shortcuts import render
from .models import Yajnas, Mantras


def yajna(request):
    yajnas = Yajnas.objects.all()
    return render(request, 'donations/yajna.html', {'yajnas': yajnas})


def charts(request):
    mantras = Mantras.objects.all()
    return render(request, 'donations/charts.html', {'mantras': mantras})


def casino(request):
    return render(request, 'donations/casino.html')


def cowshelter(request):
    return render(request, 'donations/cowshelter.html')


def donate(request):
    return render(request, 'donations/donate.html')


def gems(request):
    return render(request, 'donations/gems.html')


def marriage(request):
    return render(request, 'donations/marriage.html')
