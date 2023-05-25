from django import forms
from .models import Perro, Gato, Exotico

class PerroForm(forms.ModelForm):
    class Meta:
        model = Perro
        fields = "__all__"

class GatoForm(forms.ModelForm):
    class Meta:
        model = Gato
        fields = "__all__"

class ExoticoForm(forms.ModelForm):
    class Meta:
        model = Exotico
        fields = "__all__"        