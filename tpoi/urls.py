"""
URL configuration for tpoi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ufn import views as ufn_views
from biblioteca import views as biblioteca_views
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ufn_views.index, name="index"),
    path('crear_libro/', biblioteca_views.crear_libro, name='crear_libro'),
    path('editar_libro/<int:libro_id>', biblioteca_views.editar_libro, name='editar_libro'),
    path('eliminar_libro/<int:libro_id>', biblioteca_views.eliminar_libro, name='eliminar_libro'),
    path("contacto/", ufn_views.contacto, name="contacto"),
    path("alumnos/alumnos", ufn_views.alumnos, name="alumnos"),
    path("index/", ufn_views.index, name="index"),
    path("alumnos/calendario", ufn_views.calendario, name="calendario"),
    path("alumnos/inscripciones", ufn_views.inscripciones, name="inscripciones"),
    path("alumnos/tramites", ufn_views.tramites, name="tramites"),
    path("carrearas/carreras", ufn_views.carreras, name="carreras"),
    path("carreras/regimen", ufn_views.regimen, name="regimen"),
    path("acercade/acercade", ufn_views.acercade, name="acercade"), 
    path("acercade/autoridades", ufn_views.autoridades, name="autoridades"),
    path("acercade/sedes", ufn_views.sedes, name="sedes"),
    path("alumnos/biblioteca", biblioteca_views.biblioteca, name="biblioteca"),
    path('catalogo/', biblioteca_views.catalogo, name='catalogo'),
    path("gestion_biblioteca", biblioteca_views.gestion_biblioteca, name="gestion_biblioteca"),
    path("templategeneralpaginas", ufn_views.templategeneralpaginas, name= "templategeneralpaginas"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)