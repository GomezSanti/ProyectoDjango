from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Agregar-Perro/", views.agregar_perro, name="agregar-perro"),
    path("Agregar-Gato/", views.agregar_gato, name="agregar-gato"),
    path("Agregar-Exotico/", views.agregar_exotico, name="agregar-exotico"),
    ]
urlpatterns += staticfiles_urlpatterns()
