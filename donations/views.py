from django.core.urlresolvers import reverse
from django.shortcuts import render
from .models import Yajnas, Mantras, RudTable


def yajna(request):
    yajnas = Yajnas.objects.all()
    return render(request, 'donations/yajna.html', {'yajnas': yajnas})


def charts(request):
    mantras = Mantras.objects.all()
    return render(request, 'donations/charts.html', {'mantras': mantras})


def cowshelter(request):
    return render(request, 'donations/cowshelter.html')


def services(request):
    return render(request, 'donations/services.html')


def rudraksh(request):
    table = RudTable.objects.all()
    return render(request, 'donations/rudraksh.html', {'table': table})


def cart(request):
    return render(request, 'donations/cart.html')
