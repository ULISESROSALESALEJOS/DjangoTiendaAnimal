from django.urls import path,include
from . import views
from django.shortcuts import redirect
from productos.views import tiendaHTML,adm_productos

urlpatterns = [
    path('index',views.indexHtml, name='index'),
    path('contacto',views.contactoHTML, name='contacto'),
    path('donaciones',views.donacionesHTML, name='donaciones'),
    path('login',views.loginHTML, name='login'),
    path('nosotros',views.nosotrosHTML, name='nosotros'),
    path('registro', views.registroHTML, name ='registro'),
    path('tienda',tiendaHTML,name='tienda'),
    path('adm_prod',adm_productos,name='adm_prod'),

]
