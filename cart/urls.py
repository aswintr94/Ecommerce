from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<int:pro_id>', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('remove_item/<int:item_id>', views.remove_item, name='remove_item'),
]