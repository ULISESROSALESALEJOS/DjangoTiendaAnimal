from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductoAdd
from .models import Producto
from django.contrib.auth import authenticate,login


# Create your views here.
def tiendaHTML(request):
    return render(request,'tienda.html')

@login_required
def adm_productos(request):
    productos = Producto.objects.raw('SELECT * FROM productos_producto')
    
    if request.method == 'POST':
        formProd = ProductoAdd(request.POST)
        if formProd.is_valid():
            formProd.save()
            return redirect('adm_prod')
    else:
        formProd = ProductoAdd()

    context = { 'formProd' : formProd,'productos' : productos}
    return render(request, 'administrador_productos.html', context)

@login_required
def eliminar_producto(request, id_producto):
        producto = Producto.objects.get(id_producto=id_producto)
        producto.delete()
        return redirect('adm_prod')


    