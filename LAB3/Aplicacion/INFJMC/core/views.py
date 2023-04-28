from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    #return HttpResponse("<h1> Inicio </h1> <br> <a href=http://127.0.0.1:8000/carreras> Carreras </a> <br> <a href=http://127.0.0.1:8000/docentes> Docentes </a>")
    return render(request, 'core/home.html')
def carreras(request):
    #return HttpResponse("<h1> Carreras <br> <a href=http://127.0.0.1:8000/docentes> Docentes </a> <br> <a href=http://127.0.0.1:8000> Inicio </a>")
    return render(request, 'core/carreras.html')
def docentes(request):
    #return HttpResponse("<h1> Docentes </h1> <br> <a href=http://127.0.0.1:8000/carreras> Carreras </a> <br> <a href=http://127.0.0.1:8000> Inicio </a>")
    return render(request, 'core/docentes.html')