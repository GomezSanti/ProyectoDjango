from django import forms

from . import models

class PerroForm(forms.modelform):
    class Meta:
        model = models.Perro
        fields = "__all__"

class GatoForm(forms.modelform):
    class Meta:
        model = models.Gato
        fields = "__all__"

class ExoticoForm(forms.modelform):
    class Meta:
        model = models.Exotico
        fields = "__all__"        