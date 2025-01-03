from django import forms
from django.contrib.auth.models import User
from AppScholl.models import Asignatura,Perfil
DIAS_CHOICES = [
        ('lunes-miercoles', 'Lunes-Miercoles'),
        ('martes-jueves', 'Martes-Jueves'),
        ('miercoles-viernes', 'Miercoles-Viernes'), ]

NIVELES_CHOICES = [
        ('bajo', 'Bajo'),
        ('medio', 'Medio'),
        ('alto', 'Alto'),]

ROLES_CHOICES = [
        ('tutor', 'Tutor'),
        ('profesor', 'Profesor'),
        
        
       
    ]
   
CATEGORIAS_CHOICES = [
    ('data', 'Data'),
    ('programacion', 'Programacion'),
    ('diseño', 'Diseño'),
    ('marketing', 'Marketing')
]
HORAS_CHOICES = [
        
        
        ('12:00-14:00', '12:00-14:00 PM'),
        ('18:00-20:00', '18:00-20:00 PM'),
        ('21:00-22:30', '21:00-22:30 PM'),
    ]

class NuevoCurso(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['nombre', 'dia', 'hora', 'duracion', 'tipo', 'categoria']
    dia = forms.ChoiceField(choices=DIAS_CHOICES,label='dias')
    hora = forms.ChoiceField(choices=HORAS_CHOICES,label='hora')
    categoria = forms.ChoiceField(choices=CATEGORIAS_CHOICES,label='categoria')
    tipo = forms.ChoiceField(choices=[('curso', 'Curso')], initial='curso', label="Tipo")
    

class InicioSesion(forms.Form):
    usuario = forms.CharField(
        max_length=100, 
        label="Usuario", 
        widget=forms.TextInput(attrs={'class': 'form-usuario'})
    )
    contraseña = forms.CharField(
        max_length=100, 
        label="Contraseña", 
        widget=forms.PasswordInput(attrs={'class': 'form-contraseña'})
    )
    
class NuevaCarrera(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre del curso")
    dia = forms.ChoiceField(choices=DIAS_CHOICES, label="Día")
    hora = forms.ChoiceField(choices=HORAS_CHOICES, label="Hora")
    duracion = forms.IntegerField(min_value=1, label="Duración (en semanas)")
    tipo = forms.ChoiceField( label="tipo", choices=[('carrera','carrera')]  )
    categoria = forms.ChoiceField(choices=CATEGORIAS_CHOICES, label="Categoria")

    
    
class NuevoAlumno(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre ")    
    apellido = forms.CharField(max_length=100, label="apellido")
    dni = forms.IntegerField(label="Documento")
    cursoscom = forms.CharField(max_length=100, label="cursos/comisiones ") 
    carrera = forms.CharField(max_length=100, label="carrera ") 
    edad = forms.IntegerField(label="edad")
    
class NuevoProfesional(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre ")    
    apellido = forms.CharField(max_length=100, label="apellido")
    dni = forms.IntegerField(label="Documento")
    profesion = forms.CharField(max_length=100, label="profesion") 
    rol = forms.ChoiceField(choices=ROLES_CHOICES, label="Rol")
    presentacion = forms.CharField(max_length=500, label="presentacion ")  
    
    
class Buscar(forms.Form):
    buscador = forms.CharField(max_length=100,required=False)
    
class ActualizarUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email'] 
    
class FotoPerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto']
    