from django.urls import path

from . import views

urlpatterns = [
    path("yajna/", views.yajna, name="yajna"),
    path("charts/", views.charts, name="charts"),
    path("cowshelter/", views.cowshelter, name="cowshelter"),
    path("cart/", views.cart, name="cart"),
    path("services/", views.services, name="services"),
    path("rudraksh/", views.rudraksh, name="rudraksh"),
]
