from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^aboutus/$', views.about, name='about'),
    url(r'^contactus/$', views.contact, name='contact')
]
