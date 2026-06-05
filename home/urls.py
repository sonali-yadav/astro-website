from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("faq/", views.faq, name="faq"),
    path("aboutus/", views.about, name="about"),
    path("contactus/", views.contact, name="contact"),
]
