from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . import forms

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")

def agregar_perro(request):
    form=forms.PerroForm()
    return render(request, "home/agregar-perro.html")

def agregar_gato(request):
    form=forms.GatoForm()
    return render(request, "home/agregar-gato.html")

def agregar_perro(request):
    form=forms.ExoticoForm()
    return render(request, "home/agregar-exotico.html")