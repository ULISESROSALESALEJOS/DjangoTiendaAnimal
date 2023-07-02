from django import forms
from django.forms import ModelForm,TextInput
from .models import Producto

class ProductoAdd(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        # widgets = {
        #     'fecha_nacimiento': forms.widgets.DateInput(attrs={'type': 'date'}),
        #     'rut':forms.widgets.TextInput(attrs={'class': 'rut-css'}),
        # }