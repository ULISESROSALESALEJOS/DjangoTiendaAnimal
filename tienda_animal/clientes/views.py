from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .models import Cliente,Genero
from .forms import ClienteForm,GeneroForm

# Create your views here.

def indexHtml(request):
    return render(request,'index.html')

def loginHTML(request):
    return render(request,'login.html')

def contactoHTML(request):
    return render(request,'contacto.html')

def donacionesHTML(request):
    return render(request,'donaciones.html')

def nosotrosHTML(request):
    return render(request,'nosotros.html')

def addCliente (request):
    if request.method is not "POST":
        generos = Genero.objects.all()
        context = {'genero':generos}
        return render(request,'registro.html',context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno =request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        
        objGenero = Genero.objects.get(id_genero = genero)
        obj = Cliente.objects.create(rut = rut,
                                    nombre = nombre,
                                    apellido_paterno = aPaterno,
                                    apellido_materno = aMaterno,
                                    fecha_nacimiento = fechaNac,
                                    id_genero = objGenero,
                                    telefono = telefono,
                                    email = email,
                                    direccion = direccion
        ) 
        obj.save()
        context = {'mensaje':'Agregado Exitosamente!'}
        return render(request,'registro.html',context)