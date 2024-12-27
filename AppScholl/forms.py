from django import forms
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
TIPOS_CHOICES =[
    ('carrera', 'carrera'),
    ('curso', 'curso'),
]    
    
HORAS_CHOICES = [
        
        
        ('12:00-14:00', '12:00-14:00 PM'),
        ('18:00-20:00', '18:00-20:00 PM'),
        ('21:00-22:30', '21:00-22:30 PM'),
    ]

class NuevoCurso(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre del curso")
    dia = forms.ChoiceField(choices=DIAS_CHOICES, label="Día")
    hora = forms.ChoiceField(choices=HORAS_CHOICES, label="Hora")
    duracion = forms.IntegerField(min_value=1, label="Duración (en semanas)")
    tipo = forms.ChoiceField(choices=TIPOS_CHOICES, label="tipo")
    


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
    nivel = forms.ChoiceField(choices=NIVELES_CHOICES, label="nivel")
    tipo = forms.ChoiceField( label="tipo", initial='carrera',  widget=forms.Select(attrs={'disabled': 'disabled'}))


    
    
class NuevoAlumno(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre ")    
    apellido = forms.CharField(max_length=100, label="apellido")
    dni = forms.IntegerField(label="Documento")
    cursosycomisiones = forms.CharField(max_length=100, label="cursos/comisiones ",initial='curso:comision') 
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