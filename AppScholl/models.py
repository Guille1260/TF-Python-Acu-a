from django.db import models

# Modelo Alumno
class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    documento = models.IntegerField()
    cursoscomisiones = models.TextField() 
    carreras = models.TextField()  
    edad = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Profesional(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    documento = models.IntegerField()
    profesion = models.CharField(max_length=30)
    rol = models.CharField(max_length=30)
    presentacion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.profesion})"

class Asignatura(models.Model):
    nombre = models.CharField(max_length=30)
    dia = models.CharField(max_length=30, default='lunes-Miercoles')
    hora = models.CharField(max_length=30, default='12:00-14:30 PM')
    duracion = models.IntegerField(default=1)  # Cambié el valor por defecto a un entero
    tipo = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    usuario = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=255)  
    def __str__(self):
        return self.usuario
