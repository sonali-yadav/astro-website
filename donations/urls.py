from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^yajna/$', views.yajna, name='yajna'),
    url(r'^charts/$', views.charts, name='charts'),
    url(r'^cowshelter/$', views.cowshelter, name='cowshelter'),
    url(r'^donate/$', views.donate, name='donate'),
    url(r'^gems/$', views.gems, name='gems'),
    url(r'^marriage/$', views.marriage, name='marriage'),
]
