from django import forms
from .models import Genero,Cliente
from django.forms import ModelForm,TextInput

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut','nombre','apellido_paterno']
        
class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = ['genero']