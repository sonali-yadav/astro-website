from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^yajna/$', views.yajna, name='yajna'),
    url(r'^charts/$', views.charts, name='charts'),
    url(r'^casino/$', views.casino, name='casino'),
    url(r'^cowshelter/$', views.cowshelter, name='cowshelter'),
    url(r'^donate/$', views.donate, name='donate')
]
