from django.urls import path
from . import views

urlpatterns = [
    path('tienda',views.tiendaHTML,name='tienda'),
    path('adm_prod',views.adm_productos,name='adm_prod'),
    path('eliminar-producto/<int:id_producto>/', views.eliminar_producto, name='eliminar_producto'),
]