from django.urls import path
from . import views

urlpatterns = [
    path('tienda',views.tiendaHTML,name='tienda'),
    path('mantenedor',views.adm_productos,name='mantenedor'),
    path('eliminar-producto/<int:id_producto>/', views.eliminar_producto, name='eliminar_producto'),
    path('editar_Producto/<int:id_producto>/', views.editar_producto, name='editar_Producto'),
]