from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def indexHtml(request):
    return render(request,'index.html')
