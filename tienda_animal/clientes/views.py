from django.shortcuts import render
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

def registroHTML(request):
    return render(request,'registro.html')

# def addCliente(request):
#     cliente = ClienteForm()
#     context = {"clientes":cliente}
#     return render(request,'clientes/registro.html', context)
