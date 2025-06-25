from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from .models import Parroquia, Barrio
from .forms import BarrioForm, ParroquiaForm
from django.shortcuts import redirect

def index(request):
    """
    Render the index page of the ordenamiento app.
    """
    context = {
        'title': 'Ordenamiento Territorial',
        'message': 'Bienvenido al módulo de gestion de Ordenamiento Territorial.'
    }
    return render(request, 'ordenamiento/index.html', context)

def listar_parroquia(request):
    """
    List all parroquias.
    """
    parroquias = Parroquia.objects.all()
    
    context = {
        'parroquias': parroquias,
        'title': 'Listado de Parroquias'
    }
    
    return render(request, 'ordenamiento/listar_parroquia.html', context)

def listar_barrio(request):
    """
    List all barrios.
    """
    barrios = Barrio.objects.all()
    
    context = {
        'barrios': barrios,
        'title': 'Listado de Barrios'
    }
    
    return render(request, 'ordenamiento/listar_barrio.html', context)

def agregar_barrio(request):
    if request.method == 'POST':
        form = BarrioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_barrio')
    else:
        form = BarrioForm()

    return render(request, 'ordenamiento/agregar_barrio.html', {
        'form': form,
        'title': 'Agregar Barrio'
    })

def agregar_parroquia(request):
    if request.method == 'POST':
        form = ParroquiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_parroquia')
    else:
        form = ParroquiaForm()

    return render(request, 'ordenamiento/agregar_parroquia.html', {
        'form': form,
        'title': 'Agregar Parroquia'
    })