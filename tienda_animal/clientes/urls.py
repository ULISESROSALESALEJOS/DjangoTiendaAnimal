from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexHtml, name='index'),
    path('contacto',views.contactoHTML, name='contacto'),
    path('donaciones',views.donacionesHTML, name='contacto'),
    path('login',views.loginHTML, name='contacto'),
    path('nosotros',views.nosotrosHTML, name='contacto'),

    ##path('registro',views.registroHTML, name='registro'),
    path('registroHTML/', views.registroHTML, name = 'registro'),
    # path('clientes_add', views.addCliente,name='clientesAdd'),

]
