from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProductoAdd
from .models import Producto
from django.contrib.auth import authenticate,login


# Create your views here.
def tiendaHTML(request):
    user_admin = request.user.is_superuser
    return render(request,'tienda.html',{'user_admin':user_admin})

@login_required
def adm_productos(request):
    productos = Producto.objects.raw('SELECT * FROM productos_producto')
    user_admin = request.user.is_superuser
    
    if request.method == 'POST':
        formProd = ProductoAdd(request.POST)
        if formProd.is_valid():
            formProd.save()
            return redirect('mantenedor')
    else:
        formProd = ProductoAdd()

    context = { 'formProd' : formProd,'productos' : productos,'user_admin':user_admin}
    return render(request, 'mantenedor.html', context)

@login_required
def eliminar_producto(request, id_producto):
        producto = Producto.objects.get(id_producto=id_producto)
        producto.delete()
        return redirect('mantenedor')

@login_required
def editar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)

    if request.method == 'POST':
        form = ProductoAdd(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('mantenedor')
    else:
        form = ProductoAdd(instance=producto)

    return render(request, 'editar_Producto.html', {'form': form})