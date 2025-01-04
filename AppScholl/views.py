from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate,login as nuevo,logout
from django.shortcuts import  redirect, render
from AppScholl.models import Profesional,Alumno,Asignatura,Perfil as profile
from AppScholl.forms import NuevoCurso,InicioSesion,NuevaCarrera,NuevoAlumno,NuevoProfesional,Buscar,ActualizarUsuarioForm,FotoPerfilForm
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required

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


@login_required(login_url='Login')
def alumnos(request):
    query = request.GET.get('buscador', '')  
    buscador = Buscar(request.GET)  
    alumnos = Alumno.objects.all()
    if 'reset' in request.GET:  
        query = ''
        alumnos = Alumno.objects.all()  
    elif query:
        if query.isdigit():
            alumnos = Alumno.objects.filter(documento__icontains=query)
        else:
            alumnos = Alumno.objects.filter(apellido__icontains=query)
    if 'eliminar' in request.POST:  
        alumno_documento = request.POST.get('alumno_documento')  
        if alumno_documento:
            alumno = Alumno.objects.filter(documento=alumno_documento).first()
            if alumno:
                alumno.delete()
            else:
                from django.contrib import messages
                return redirect('Alumnos')
    return render(request, 'AppScholl/alumnos.html', {'alumnos': alumnos,  'buscar': buscador,   'query': query  })
    
    
    
    
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
        profesionales = Profesional.objects.filter(documento__icontains=query)  
    if 'eliminar' in request.POST: 
        profesional_documento = request.POST.get('profesional_documento')  
        if profesional_documento:
            profesional = Profesional.objects.filter(documento=profesional_documento).first()  
            if profesional:
                profesional.delete()  
            else:
                return redirect('Profesionales')  
    return render(request, 'AppScholl/profesionales.html', {'profesionales': profesionales,  'buscar': buscador,  'query': query,  'filtro': filtro, })

@login_required(login_url='Login')
def Perfil(request):
    usuario = request.user
    icono, _ = profile.objects.get_or_create(user=usuario)
    if request.method == "POST":
        form =ActualizarUsuarioForm(request.POST,instance=usuario)
        perfil_form = FotoPerfilForm(request.POST,request.FILES,instance=icono)
        if form.is_valid() and perfil_form.is_valid():
            form.save()
            perfil_form.save()
            return redirect('Home')
        else:
            return redirect('Perfil')
    else:
        form =ActualizarUsuarioForm(instance=usuario)
        perfil_form = FotoPerfilForm(instance=icono)
    return render(request,'AppScholl/perfil.html',{'form':form,'perfil':perfil_form})


@login_required(login_url='Login')
def CambiarContraseña(request):
    usuario = request.user  # Obtiene el usuario actual
    if request.method == 'POST':
        form = PasswordChangeForm(user=usuario, data=request.POST)
        if form.is_valid():  
            form.save()  
            return redirect('Home')  
        else:
            return redirect('Cursos')
    else:
       
        form = PasswordChangeForm(user=usuario)

    return render(request, 'AppScholl/cambio.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = InicioSesion(request.POST) 
        if form.is_valid():
            username = form.cleaned_data['usuario']
            password = form.cleaned_data['contraseña']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                nuevo(request,user)
                return redirect('Home')  
            else:
                return render(request, 'AppScholl/login.html', {'form': form,'mensaje': 'usuario o contraseña no existen'})
    else:
        form = InicioSesion()  
    
    return render(request, 'AppScholl/login.html', {'form': form})
    
def user_logaut(request):
    logout(request)
    return redirect('Home')  

@login_required(login_url='Login')
def Nuevo_usuario(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = UserCreationForm()
    return render(request, 'AppScholl/registro.html',{'form':form})

# vistas agregar
@login_required(login_url='Login')
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

@login_required(login_url='Login')
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

@login_required(login_url='Login')
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

@login_required(login_url='Login')
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

@login_required(login_url='Login')
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

@login_required(login_url='Login')
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

@login_required(login_url='Login')
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

@login_required(login_url='Login')
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