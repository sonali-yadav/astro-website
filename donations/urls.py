from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^yajna/$', views.yajna, name='yajna'),
    url(r'^charts/$', views.charts, name='charts'),
    url(r'^cowshelter/$', views.cowshelter, name='cowshelter'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^services/$', views.services, name='services'),
    url(r'^rudraksh/$', views.rudraksh, name='rudraksh'),
]
