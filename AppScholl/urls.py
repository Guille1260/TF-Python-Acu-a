from django.contrib import admin
from django.urls import path
from AppScholl import views

urlpatterns = [
    path("",views.inicio,name='Home'),
    path("cursos/",views.curso,name='Cursos'),
    path("carreras/",views.carreras,name='Carreras'),
    path("alumnos/",views.alumnos,name='Alumnos'),
    path("profesionales/",views.profesionales,name='Profesionales'),
    path("login/",views.login,name='Login'),
   
    path("nuevocurso/",views.AddCurso,name='AddCurso'),
    path("nuevacarrera/",views.AddCarrera,name='AddCarrera'),
    path("nuevoalumno/",views.AddAlumno,name='AddAlumno'),
    path("nuevoprofesional/",views.AddAProfesional,name='AddProfesional'),
    path("modificarcurso/<str:curso_nombre>",views.ModCurso,name='ModCurso'),
    path("modificarcarrera/<str:carrera_nombre>",views.ModCarrera,name='ModCarrera'),
    path("modificaralumno/<int:alumno_documento>",views.ModAlumno,name='ModAlumno'),
    path("modificarprofesional/<int:profesional_documento>",views.ModProfesional,name='ModProfesional'),
     
]