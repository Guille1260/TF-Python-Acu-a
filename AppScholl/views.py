from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from AppScholl.models import Profesional,Alumno,Asignatura
from AppScholl.forms import NuevoCurso,InicioSesion,NuevaCarrera,NuevoAlumno,NuevoProfesional,Buscar


def inicio(request):
    cursos = Asignatura.objects.filter(tipo='curso') 
    carrera = Asignatura.objects.filter(tipo='carrera') 
    profesional = Profesional.objects.all()
    return render(request,'AppScholl/inicio.html',{'profesionales':profesional,'cursos': cursos,'carreras':carrera})

def curso(request):
    query = request.GET.get('buscador') 
    filtro = request.GET.get('filtro')  
    buscador = Buscar(request.GET)  
    if 'reset' in request.GET:
        query = '' 
        cursos = Asignatura.objects.filter(tipo='curso') 
    elif filtro:  
        cursos = Asignatura.objects.filter(tipo='curso', categoria__icontains=filtro)  
    elif query:  
        cursos = Asignatura.objects.filter(tipo='curso', nombre__icontains=query)  
    else:
        cursos = Asignatura.objects.filter(tipo='curso')  
    if 'eliminar' in request.POST:
        curso_nombre = request.POST.get('curso_nombre')  
        if curso_nombre:
            curso = Asignatura.objects.filter(nombre=curso_nombre).first() 
            if curso:
                curso.delete()  
            else:
                pass
            return redirect('Cursos') 
    return render(request, 'AppScholl/cursos.html', {'cursos': cursos,'buscar': buscador,'query': query,'filtro': filtro})

def carreras(request):
    query = request.GET.get('buscador') 
    filtro = request.GET.get('filtro')  
    buscador = Buscar(request.GET)  
    if 'reset' in request.GET:
        query = '' 
        carrera = Asignatura.objects.filter(tipo='carrera')
    elif filtro:  
        carrera = Asignatura.objects.filter(tipo='carrera', categoria__icontains=filtro)  
    elif query:  
        carrera = Asignatura.objects.filter(tipo='carrera', nombre__icontains=query)  
    else:
        carrera = Asignatura.objects.filter(tipo='carrera')
     
    if 'eliminar' in request.POST:
        carrera_nombre = request.POST.get('carrera_nombre')  
        if carrera_nombre:
            carrera= Asignatura.objects.filter(nombre=carrera_nombre).first() 
            if curso:
                carrera.delete()  
            else:
                pass
            return redirect('Carreras') 
    return render(request,'AppScholl/carreras.html',{'carreras':carrera,'buscar':buscador,'query': query,'filtro': filtro})



def alumnos(request):
    query = request.GET.get('buscador', '')  # Asegúrate de que query tenga un valor predeterminado
    buscador = Buscar(request.GET)  # Suponiendo que tienes un formulario 'Buscar' para el filtro
    
    # Inicializamos la variable 'alumnos' por defecto con todos los alumnos
    alumnos = Alumno.objects.all()
    
    # Si se hace un reset, borrar el valor de la búsqueda
    if 'reset' in request.GET:  
        query = ''
        alumnos = Alumno.objects.all()  # Mostrar todos los alumnos si no hay búsqueda
    elif query:
        # Si la búsqueda es un número, buscar por 'documento', sino buscar por 'apellido'
        if query.isdigit():
            alumnos = Alumno.objects.filter(documento__icontains=query)
        else:
            alumnos = Alumno.objects.filter(apellido__icontains=query)
    
    # Manejo de eliminación de un alumno
    if 'eliminar' in request.POST:  
        alumno_documento = request.POST.get('alumno_documento')  
        if alumno_documento:
            alumno = Alumno.objects.filter(documento=alumno_documento).first()
            if alumno:
                alumno.delete()
            else:
                # Puedes agregar un mensaje aquí si el alumno no fue encontrado
                # Ejemplo con el sistema de mensajes de Django
                from django.contrib import messages
                messages.error(request, "Alumno no encontrado.")
                return redirect('Alumnos')
    
    # Pasar los datos a la plantilla
    return render(request, 'AppScholl/alumnos.html', {
        'alumnos': alumnos,  
        'buscar': buscador,   
        'query': query  
    })
    
    
    
    
def profesionales(request):
    query = request.GET.get('buscador')  
    filtro = request.GET.get('filtro')  
    buscador = Buscar(request.GET)  
    profesionales = Profesional.objects.all()  
    if 'reset' in request.GET:  
        query = ''  
        filtro = ''  
        profesionales = Profesional.objects.all()  
    elif filtro:  
        profesionales = Profesional.objects.filter(rol__icontains=filtro)  
    elif query:  
        profesionales = Profesional.objects.filter(nombre__icontains=query)  
    if 'eliminar' in request.POST: 
        profesional_documento = request.POST.get('profesional_documento')  
        if profesional_documento:
            profesional = Profesional.objects.filter(documento=profesional_documento).first()  
            if profesional:
                profesional.delete()  
            else:
                return redirect('Profesionales')  
    return render(request, 'AppScholl/profesionales.html', {'profesionales': profesionales,  'buscar': buscador,  'query': query,  'filtro': filtro, })



def login(request):
    log = InicioSesion
    return render(request,'AppScholl/login.html',{'login':log})




# vistas agregar
def AddCurso(request):
    if request.method == 'POST':
        formularioadd = NuevoCurso(request.POST)  
        if formularioadd.is_valid():
            nombre = formularioadd.cleaned_data['nombre']
            dia = formularioadd.cleaned_data['dia']
            hora = formularioadd.cleaned_data['hora']
            duracion = formularioadd.cleaned_data['duracion']
            tipo = formularioadd.cleaned_data['tipo']
            categoria = formularioadd.cleaned_data['categoria']
            asignatura = Asignatura(
                nombre=nombre,
                dia=dia,
                hora=hora,
                duracion=duracion,
                tipo=tipo,
                categoria=categoria
            )
            asignatura.save()  
            return redirect('AddCurso')  
        else:
            return render(request, 'AppScholl/components/addcurso.html', {'form': formularioadd})
    else:
        formularioadd = NuevoCurso()
        return render(request, 'AppScholl/components/addcurso.html', {'form': formularioadd})

def AddCarrera(request):
    if request.method == 'POST':
        formularioadd = NuevaCarrera(request.POST)  
        if formularioadd.is_valid():
            nombre = formularioadd.cleaned_data['nombre']
            dia = formularioadd.cleaned_data['dia']
            hora = formularioadd.cleaned_data['hora']
            duracion = formularioadd.cleaned_data['duracion']
            tipo = formularioadd.cleaned_data['tipo']
            categoria = formularioadd.cleaned_data['categoria']
            asignatura = Asignatura(
                nombre=nombre,
                dia=dia,
                hora=hora,
                duracion=duracion,
                tipo=tipo,
                categoria=categoria
            )
            asignatura.save()  
            return redirect('AddCarrera')  
        else:
            return render(request, 'AppScholl/components/addcarrera.html', {'form': formularioadd})
    else:
        formularioadd = NuevaCarrera()
        return render(request, 'AppScholl/components/addcarrera.html', {'form': formularioadd})

def AddAlumno(request):
    if request.method == 'POST':
        formularioadd = NuevoAlumno(request.POST)  
        if formularioadd.is_valid():
            nombre = formularioadd.cleaned_data['nombre']
            apellido = formularioadd.cleaned_data['apellido']
            documento = formularioadd.cleaned_data['dni']
            cursoscom = formularioadd.cleaned_data['cursoscom']
            carrera = formularioadd.cleaned_data['carrera']
            edad = formularioadd.cleaned_data['edad']
            alumno = Alumno(
                nombre=nombre,
                apellido=apellido,
                documento=documento,
                cursoscomisiones =cursoscom,
                carreras=carrera,
                edad=edad
            )
            alumno.save()  
            return redirect('AddAlumno')  
        else:
            return render(request, 'AppScholl/components/addalumno.html', {'form': formularioadd})
    else:
        formularioadd = NuevoAlumno()
        return render(request, 'AppScholl/components/addalumno.html', {'form': formularioadd})

def AddAProfesional(request):
    if request.method == 'POST':
        formularioadd = NuevoProfesional(request.POST)  
        if formularioadd.is_valid():
            nombre = formularioadd.cleaned_data['nombre']
            apellido = formularioadd.cleaned_data['apellido']
            documento = formularioadd.cleaned_data['dni']
            profesion = formularioadd.cleaned_data['profesion']
            rol = formularioadd.cleaned_data['rol']
            presentacion = formularioadd.cleaned_data['presentacion']
            profesional = Profesional(
                nombre=nombre,
                apellido=apellido,
                documento=documento,
                profesion=profesion,
                rol=rol ,
                presentacion=presentacion
            )
            profesional.save()  
            return redirect('AddProfesional')  
        else:
            return render(request, 'AppScholl/components/addprofesional.html', {'form': formularioadd})
    else:
        formularioadd = NuevoProfesional()
        return render(request, 'AppScholl/components/addprofesional.html', {'form': formularioadd})

def ModCurso(request, curso_nombre):
    curso = get_object_or_404(Asignatura, nombre=curso_nombre)
    if request.method == 'GET':
        formulariomod = NuevoCurso(initial={
            'nombre': curso.nombre,
            'dia': curso.dia,
            'hora': curso.hora,
            'duracion': curso.duracion,
            'tipo': curso.tipo,
            'categoria': curso.categoria
        })
    else:
        formulariomod = NuevoCurso(request.POST)
        if formulariomod.is_valid():
            curso.nombre = formulariomod.cleaned_data['nombre']
            curso.dia = formulariomod.cleaned_data['dia']
            curso.hora = formulariomod.cleaned_data['hora']
            curso.duracion = formulariomod.cleaned_data['duracion']
            curso.tipo = formulariomod.cleaned_data['tipo']
            curso.categoria = formulariomod.cleaned_data['categoria']
            curso.save()  
            return redirect('AddCurso')  
    return render(request, 'AppScholl/components/modcurso.html', {'form': formulariomod, 'curso': curso})


def ModCarrera(request, carrera_nombre):
    carrera = get_object_or_404(Asignatura, nombre=carrera_nombre)
    if request.method == 'POST':
        form = NuevaCarrera(request.POST)
        if form.is_valid():
            carrera.nombre = form.cleaned_data['nombre']
            carrera.dia = form.cleaned_data['dia']
            carrera.hora = form.cleaned_data['hora']
            carrera.duracion = form.cleaned_data['duracion']
            carrera.tipo = form.cleaned_data['tipo']
            carrera.categoria = form.cleaned_data['categoria']
            carrera.save()
            return redirect('Carreras')  
    else:
        
        form = NuevaCarrera(initial={
            'nombre': carrera.nombre,
            'dia': carrera.dia,
            'hora': carrera.hora,
            'duracion': carrera.duracion,
            'tipo': carrera.tipo,
            'categoria': carrera.categoria
        })
    
    return render(request, 'AppScholl/components/modcarrera.html', {'form': form, 'carrera': carrera})
def ModAlumno(request, alumno_documento):
    alumno = get_object_or_404(Alumno, documento=alumno_documento)
    if request.method == 'POST':
        form = NuevoAlumno(request.POST)  
        if form.is_valid():
            alumno.nombre = form.cleaned_data['nombre']
            alumno.apellido = form.cleaned_data['apellido']
            alumno.documento= form.cleaned_data['dni']
            alumno.cursoscomisiones = form.cleaned_data['cursoscom']
            alumno.carreras = form.cleaned_data['carrera']
            alumno.edad = form.cleaned_data['edad']
            alumno.save()
            return redirect('Alumnos') 
    else:
        form = NuevoAlumno(initial={
            'nombre': alumno.nombre,
            'apellido': alumno.apellido,
            'dni': alumno.documento,
            'cursoscom': alumno.cursoscomisiones,
            'carrera': alumno.carreras,
            'edad': alumno.edad
        })
    
    return render(request, 'AppScholl/components/modalumno.html', {'form': form, 'alumno': alumno})
4
def ModProfesional(request, profesional_documento):
    profesional = get_object_or_404(Profesional, documento=profesional_documento)
    if request.method == 'POST':
        form = NuevoProfesional(request.POST)
        if form.is_valid():
            profesional.nombre = form.cleaned_data['nombre']
            profesional.apellido = form.cleaned_data['apellido']
            profesional.documento = form.cleaned_data['dni']
            profesional.profesion = form.cleaned_data['profesion']
            profesional.rol = form.cleaned_data['rol']
            profesional.presentacion = form.cleaned_data['presentacion']
            profesional.save()
            return redirect('Profesionales') 
    else:
        form = NuevoProfesional(initial={
            'nombre': profesional.nombre,
            'apellido': profesional.apellido,
            'dni': profesional.documento,
            'profesion': profesional.profesion,
            'rol': profesional.rol,
            'presentacion': profesional.presentacion
        })
    return render(request, 'AppScholl/components/modprofesional.html', {'form': form, 'profesional': profesional})