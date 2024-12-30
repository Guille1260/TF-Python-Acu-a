from django.contrib import admin
from django.urls import path
from AppScholl import views

urlpatterns = [
    path("", views.InicioView.as_view(), name='Home'),
    path("cursos/", views.CursoListView.as_view(), name='Cursos'),
    path("carreras/", views.CarreraListView.as_view(), name='Carreras'),
    path("alumnos/", views.AlumnoListView.as_view(), name='Alumnos'),
    path("profesionales/", views.ProfesionalListView.as_view(), name='Profesionales'),
    path("login/",views.login,name='Login'),
   
    path("nuevocurso/", views.AddCursoView.as_view(), name='AddCurso'),
    path("nuevacarrera/", views.AddCarreraView.as_view(), name='AddCarrera'),
    path("nuevoalumno/", views.AddAlumnoView.as_view(), name='AddAlumno'),
    path("nuevoprofesional/", views.AddProfesionalView.as_view(), name='AddProfesional'),
    
    path("modificarcurso/<str:curso_nombre>/", views.ModCursoView.as_view(), name='ModCurso'),
    path("modificarcarrera/<str:carrera_nombre>/", views.ModCarreraView.as_view(), name='ModCarrera'),
    path("modificaralumno/<int:alumno_documento>/", views.ModAlumnoView.as_view(), name='ModAlumno'),
    path("modificarprofesional/<int:profesional_documento>/", views.ModProfesionalView.as_view(), name='ModProfesional'),
     
]