from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name= 'register'),
    path('logout/', views.logout, name='logout'),
    path('add_product/', views.add_product, name='add_product'),
    path('view_product/<int:int_id>', views.view_product, name='view_product'),
]