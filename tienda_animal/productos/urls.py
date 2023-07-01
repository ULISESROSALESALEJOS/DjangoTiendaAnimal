from django.urls import path
from . import views

urlpatterns = [
    path('tienda',views.tiendaHTML,name='tienda'),
]