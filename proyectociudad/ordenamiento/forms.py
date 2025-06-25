from django import forms
from .models import Parroquia, Barrio

class ParroquiaForm(forms.ModelForm):
    class Meta:
        model = Parroquia
        fields = ['nombre', 'ubicacion', 'tipo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ubicacion': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
        }

class BarrioForm(forms.ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre', 'num_viviendas', 'num_parques', 'num_edificios', 'parroquia']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'num_viviendas': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_parques': forms.Select(attrs={'class': 'form-control'}),
            'num_edificios': forms.NumberInput(attrs={'class': 'form-control'}),
            'parroquia': forms.Select(attrs={'class': 'form-control'}),
        }