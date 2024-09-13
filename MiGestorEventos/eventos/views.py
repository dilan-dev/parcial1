from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventoForm
from django.contrib import messages
from .models import Eventos, Organizador
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def crear_evento(request): 
    if request.method == 'POST':
        form = EventoForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Evento creado con éxito')

            return redirect(ver_eventos)
        else:
            messages.error(request, 'Error al crear evento')
    else:
        form = EventoForm()
        
    return render (request, 'crear_eventos.html', {'form': form})


def ver_eventos(request):

    eventos = Eventos.objects.all()

    return render(request, 'ver_eventos.html', {'eventos': eventos})


def index(request):
    return render(request, 'index.html', {'mensaje': "mandril además"})


class OrganizadorListView(ListView):

    model = Organizador
    template_name = 'organizadores.html'
    context_object_name = 'organizadores'

class OrganizadorCreateView(CreateView):
    model = Organizador
    template_name = 'organizador-form.html'
    fields = ['nombre', 'email', 'telefono', 'direccion']
    success_url = reverse_lazy('organizador-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['nombre'].widget = forms.TextInput(attrs={'class': 'form-control'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control'})
        form.fields['telefono'].widget = forms.TextInput(attrs={'class': 'form-control'})
        form.fields['direccion'].widget = forms.Textarea(attrs={'class': 'form-control'})
        return form


def loginPanel(request):
    page = 'login'
    error_message = None

    if request.method == 'POST':

        username = request.POST.get('usuario')
        password = request.POST.get('pass')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('ver_eventos')
        else:
            error_message = 'Credenciales inválidas'
    return render(request, 'user-login.html', {'error_message': error_message, 'page':page})


def logoutUser(request):
    logout(request)
    return redirect('index')


@login_required(login_url=loginPanel)
def editar_evento(request, id):
    evento = get_object_or_404(Eventos, id=id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('ver_eventos') 
    else:
        form = EventoForm(instance=evento)
    
    return render(request, 'editar_evento.html', {'form': form, 'evento':evento})

