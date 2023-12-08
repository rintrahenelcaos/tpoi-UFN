from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request,"index.html")

def contacto(request):
    
    return render(request, "contacto.html")

def alumnos(request):
    return render(request, "alumnos/alumnos.html")


def calendario(request):
    
    return render(request, "alumnos/calendario.html")

def inscripciones(request):
    return render(request, "alumnos/inscripciones.html")

def tramites(request):
    return render(request, "alumnos/tramites.html")

def carreras(request):
    return render(request, "carreras/carreras.html")

def regimen(request):
    return render(request, "carreras/regimen.html")

def acercade(request):
    return render(request, "acercade/acercade.html")

def autoridades(request):
    return render(request, "acercade/autoridades.html")

def sedes(request):
    return render(request, "acercade/sedes.html")

def biblioteca(request):
    return render(request, "alumnos/biblioteca.html")

