from django.shortcuts import render
from .models import Yajnas, Mantras, Rudraksh, RudTable


def yajna(request):
    yajnas = Yajnas.objects.all()
    return render(request, 'donations/yajna.html', {'yajnas': yajnas})


def charts(request):
    mantras = Mantras.objects.all()
    return render(request, 'donations/charts.html', {'mantras': mantras})


def cowshelter(request):
    return render(request, 'donations/cowshelter.html')


def donate(request):
    return render(request, 'donations/donate.html')


def gems(request):
    return render(request, 'donations/gems.html')


def marriage(request):
    return render(request, 'donations/marriage.html')


def rudraksh(request):
    ruds = Rudraksh.objects.all()
    table = RudTable.objects.all()
    return render(request, 'donations/rudraksh.html', {'ruds': ruds, 'table': table})
