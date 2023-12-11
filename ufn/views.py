from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from .models import Libro

def index(request):
    return render(request, "index.html")

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
    libros = Libro.objects.all()
    
    return render(request, 'alumnos/biblioteca.html', {'libros': libros})

def gestion_biblioteca(request):
    libros = Libro.objects.all()
    return render(request, "gestion_biblioteca.html", {'libros': libros})
    




def crear_libro(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        temas = request.POST['temas']
        dispon = request.POST['dispon']
        
        Libro.objects.create(titulo=titulo, autor=autor, temas=temas, dispon=dispon) 
        return redirect('gestion_biblioteca')

    return render(request, 'crear_libro.html')

def catalogo(request):
    libros = Libro.objects.all()
    return render(request, 'catalogo.html', {'libros': libros})


def editar_libro(request, libro_id):
    libro = Libro.objects.get(id=libro_id)

    if request.method == 'POST':

        titulo = request.POST['titulo']
        autor = request.POST['autor']
        temas = request.POST['temas']
        dispon = request.POST['dispon']

        libro.titulo = titulo
        libro.autor = autor
        libro.temas = temas
        libro.dispon = dispon

        libro.save()


        return redirect('gestion_biblioteca')

    return render(request, 'editar_libro.html', {'libro': libro})


def eliminar_libro(request, libro_id):
    libro = Libro.objects.get(id=libro_id)

    if request.method == 'POST':

        libro.delete()

    
        return redirect('gestion_biblioteca')

    return render(request, 'eliminar_libro.html', {'libro': libro})
