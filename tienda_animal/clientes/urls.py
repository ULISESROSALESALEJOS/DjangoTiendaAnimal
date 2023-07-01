from django.urls import path,include
from . import views
from productos.views import tiendaHTML

urlpatterns = [
    path('',views.indexHtml, name='index'),
    path('contacto',views.contactoHTML, name='contacto'),
    path('donaciones',views.donacionesHTML, name='donaciones'),
    path('login',views.loginHTML, name='login'),
    path('nosotros',views.nosotrosHTML, name='nosotros'),
    path('registro', views.registroHTML, name ='registro'),
    path('registro', views.registroHTML, name ='registro'),
    path('tienda',tiendaHTML,name='tienda'),
]
