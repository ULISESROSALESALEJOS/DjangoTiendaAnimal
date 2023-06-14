from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexHtml, name='index'),
]
