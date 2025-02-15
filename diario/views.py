from django.shortcuts import render, redirect, get_object_or_404
from .models import Entrada
from .forms import EscritorForm, TemaForm, EntradaForm, BuscarEntradaForm

def agregar_escritor(request):
    if request.method == "POST":
        form = EscritorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EscritorForm()
    return render(request, 'diario/formulario.html', {'form': form, 'titulo': 'Nuevo Escritor'})

def agregar_tema(request):
    if request.method == "POST":
        form = TemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = TemaForm()
    return render(request, 'diario/formulario.html', {'form': form, 'titulo': 'Nuevo Tema'})

def agregar_entrada(request):
    if request.method == "POST":
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EntradaForm()
    return render(request, 'diario/formulario.html', {'form': form, 'titulo': 'Nueva Entrada'})

def buscar_entrada(request):
    form = BuscarEntradaForm(request.GET)
    entradas = []
    if form.is_valid():
        titulo = form.cleaned_data.get('titulo')
        if titulo:
            entradas = Entrada.objects.filter(titulo__icontains=titulo)
    return render(request, 'diario/buscar.html', {'form': form, 'entradas': entradas})

def ver_entrada(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    return render(request, 'diario/detalle_entrada.html', {'entrada': entrada})
