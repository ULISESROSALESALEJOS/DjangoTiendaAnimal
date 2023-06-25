from django import forms
from .models import Genero,Cliente
from django.forms import ModelForm,TextInput

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {'fecha_nacimiento':forms.DateInput(attrs={'type':'date'})}
        
class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = ['genero']