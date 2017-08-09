from .models import Academia, Atleta, Preta
from django.shortcuts import render

def index(request):
    return render(request, 'filiados/index.html')

def academias(request):
    todas_academias = Academia.objects.all()
    return render(request,'filiados/academias.html', {'todas_academias': todas_academias})

def atletas(request):
    todos_atletas = Atleta.objects.all()
    return render(request, 'filiados/atletas.html', {'todos_atletas': todos_atletas})

def pretas(request):
    todos_pretas = Preta.objects.all()
    return render(request, 'filiados/pretas.html', {'todos_pretas': todos_pretas})