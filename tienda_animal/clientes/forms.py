from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Cliente,Genero
from django.forms import ModelForm,TextInput

class ClienteAdd(ModelForm):
	class Meta:
		model = Cliente
		fields = '__all__'
		widgets = {
			'fecha_nacimiento': forms.widgets.DateInput(attrs={'type': 'date'}),
			'rut':forms.widgets.TextInput(attrs={'class': 'rut-css'}),
		}

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {k:"" for k in fields }

class LoginForm(AuthenticationForm):
		username = forms.CharField(label="Usuario")
		password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

