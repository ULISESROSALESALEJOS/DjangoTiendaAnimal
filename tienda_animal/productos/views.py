from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def tiendaHTML(request):
    return render(request,'tienda.html')

@login_required
def adm_productos(request):
    return render(request,'administrador_productos.html')