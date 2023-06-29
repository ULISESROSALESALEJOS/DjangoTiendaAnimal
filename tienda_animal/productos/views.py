from django.shortcuts import render

# Create your views here.
def tiendaHTML(request):
    return render(request,'tienda.html')