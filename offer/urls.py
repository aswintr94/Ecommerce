from django.urls import path
from . import views

urlpatterns = [
    path('add_offer/', views.add_offer, name='add_offer'),
]