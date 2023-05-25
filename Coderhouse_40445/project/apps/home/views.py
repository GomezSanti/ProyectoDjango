from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect 
from . import forms
from .models import Perro,Gato,Exotico

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")

def agregar_perro(request):
    if request.method == "POST":
         form = forms.PerroForm(request.POST)
         if form.is_valid():
             form.save()
         return redirect("index")
    else:
        form= forms.PerroForm()
    context={"form": form}
    return render(request, "home/agregar-perro.html", context)
def agregar_gato(request):
    if request.method == "POST":
         form = forms.GatoForm(request.POST)
         if form.is_valid():
             form.save()
         return redirect("index")
    else:
        form= forms.GatoForm()
    context={"form": form}
    return render(request, "home/agregar-gato.html", context)

def agregar_exotico(request):
    if request.method == "POST":
         form = forms.ExoticoForm(request.POST)
         if form.is_valid():
             form.save()
         return redirect("index")
    else:
        form= forms.ExoticoForm()
    context={"form": form}
    return render(request, "home/agregar-exotico.html", context)