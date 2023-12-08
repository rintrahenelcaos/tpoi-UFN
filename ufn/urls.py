from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contacto/", views.contacto, name="contacto"),
    path("alumnos/alumnos", views.alumnos, name="alumnos"),
    path("index/", views.index, name="index"),
    path("alumnos/calendario", views.calendario, name="calendario"),
    path("alumnos/inscripciones", views.inscripciones, name="inscripciones"),
    path("alumnos/tramites", views.tramites, name="tramites"),
    path("carrearas/carreras", views.carreras, name="carreras"),
    path("carreras/regimen", views.regimen, name="regimen"),
    path("acercade/acercade", views.acercade, name="acercade"), 
    path("acercade/autoridades", views.autoridades, name="autoridades"),
    path("acercade/sedes", views.sedes, name="sedes"),
    path("alumnos/biblioteca", views.biblioteca, name="biblioteca"),
    
]
