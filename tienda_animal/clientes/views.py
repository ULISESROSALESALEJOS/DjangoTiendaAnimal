from django.shortcuts import render, redirect
from .forms import UserRegisterForm,ClienteAdd
from .models import Cliente,Genero
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import messages


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
		if request.method == 'POST':
			form = ClienteAdd(request.POST)
			if form.is_valid():
				form.save()
				return redirect('index')
		else:
			form = ClienteAdd()
		
		context = { 'form' : form}
		return render(request, 'registro.html', context)

# def addCliente(request):
#     cliente = ClienteForm()
#     context = {"clientes":cliente}
#     return render(request,'clientes/registro.html', context)

