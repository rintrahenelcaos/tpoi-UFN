from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from .models import Empleado 

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
    return render(request, "alumnos/biblioteca.html")


from django.shortcuts import render, redirect
from .models import Empleado 

def crear_empleado(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        Empleado.objects.create(nombre=nombre, ...) 
        return redirect('lista_empleados')

    return render(request, 'formulario_crear_empleado.html')

def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'lista_empleados.html', {'empleados': empleados})


def editar_empleado(request, empleado_id):
    empleado = Empleado.objects.get(id=empleado_id)

    if request.method == 'POST':

        nombre = request.POST['nombre']

        empleado.nombre = nombre

        empleado.save()


        return redirect('lista_empleados')

    return render(request, 'formulario_editar_empleado.html', {'empleado': empleado})


def eliminar_empleado(request, empleado_id):
    empleado = Empleado.objects.get(id=empleado_id)

    if request.method == 'POST':

        empleado.delete()

    
        return redirect('lista_empleados')

    return render(request, 'confirmar_eliminar_empleado.html', {'empleado': empleado})
