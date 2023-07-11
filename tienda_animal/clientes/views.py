from django.shortcuts import render, redirect
from .forms import UserRegisterForm,ClienteAdd,LoginForm
from .models import Cliente,Genero
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login


# Create your views here.

def indexHtml(request):
    return render(request,'index.html')

def contactoHTML(request):
    return render(request,'contacto.html')

def donacionesHTML(request):
    return render(request,'donaciones.html')

def nosotrosHTML(request):
    return render(request,'nosotros.html')

def registroHTML(request):
    if request.method == 'POST':
        form = ClienteAdd(request.POST)
        formUser = UserRegisterForm(request.POST)
        if form.is_valid() and formUser.is_valid():
            form.save()
            formUser.save()
            
            messages.success(request, '¡Registro exitoso!')

            return redirect('index')
    else:
        form = ClienteAdd()
        formUser = UserRegisterForm()

    context = { 'form': form, 'formUser': formUser }
    return render(request, 'registro.html', context)

def loginHTML(request):
    if request.method == 'POST':
        formLogin = LoginForm(request, data=request.POST)
        if formLogin.is_valid():
            username = formLogin.cleaned_data['username']
            password = formLogin.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                print("None")
                pass
    else:
        formLogin = LoginForm(request)
        context = {'form': formLogin}
        return render(request, 'login.html', context)



