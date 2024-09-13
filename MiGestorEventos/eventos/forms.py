from django import forms
from .models import Eventos
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class EventoForm(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = ['organizador', 'titulo', 'descripcion', 'fecha', 'capacidad', 'lugar', 'estado']
        widgets = {
            'organizador': forms.Select(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'lugar': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

    
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if titulo.lower() == 'cancelado' :
            raise forms.ValidationError("El título no puede contener la palabra 'Cancelado'")
        return titulo
    
    
