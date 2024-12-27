from django.shortcuts import render
from AppScholl.models import Profesional,Alumno,Asignatura
from AppScholl.forms import NuevoCurso,InicioSesion,NuevaCarrera,NuevoAlumno,NuevoProfesional,Buscar
# Create your views here.
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

    return render(request, 'AppScholl/cursos.html', {'cursos': cursos, 'buscar': buscador, 'query': query, 'filtro': filtro})






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
     
    return render(request,'AppScholl/carreras.html',{'carreras':carrera,'buscar':buscador,'query': query,'filtro': filtro})



def alumnos(request):
    query = request.GET.get('buscador')  
    buscador = Buscar(request.GET)  
    if 'reset' in request.GET:
        query = ''  
        alumnos = Alumno.objects.all()  
    elif query:  
       
        if query.isdigit():  
            alumnos = Alumno.objects.filter(documento__icontains=query)
        else:  
            alumnos = Alumno.objects.filter(apellido__icontains=query)
    else:  
        alumnos = Alumno.objects.all()

    return render(request, 'AppScholl/alumnos.html', {'alumnos': alumnos, 'buscar': buscador, 'query': query})



def profesionales(request):
    query = request.GET.get('buscador') 
    filtro = request.GET.get('filtro')  
    buscador = Buscar(request.GET)  
    if 'reset' in request.GET:
        query = '' 
        profesional = Profesional.objects.all() 
    elif filtro:  
        profesional = Profesional.objects.filter( rol__icontains=filtro)  
    elif query:  
        profesional = Profesional.objects.filter( nombre__icontains=query)  
    else:
        profesional = Profesional.objects.all() 
     
    return render(request,'AppScholl/profesionales.html',{'profesionales':profesional,'buscar':buscador,'query': query,'query': query})

def login(request):
    log = InicioSesion
    return render(request,'AppScholl/login.html',{'login':log})




# vistas agregar
def AddCurso(request):
    formularioadd = NuevoCurso()
    return render(request,'AppScholl/components/addcurso.html',{'form':formularioadd})
def AddCarrera(request):
    agregar = NuevaCarrera()
    return render(request,'AppScholl/components/addcarrera.html',{'form':agregar})
def AddAlumno(request):
    formu = NuevoAlumno()
    return render(request,'AppScholl/components/addalumno.html',{'form':formu})
def AddAProfesional(request):
    formu = NuevoProfesional()
    return render(request,'AppScholl/components/addprofesional.html',{'form':formu})
 
 
 
 
# vistas modificar
def ModCurso(request):
    formulariomod =  NuevoCurso()
    return render(request,'AppScholl/components/modcurso.html',{'form':formulariomod})
def ModCarrera(request):
    addcarrera =  NuevaCarrera()
    return render(request,'AppScholl/components/modcarrera.html',{'form':addcarrera})

def ModAlumno(request):
    formu = NuevoAlumno()
    return render(request,'AppScholl/components/modalumno.html',{'form':formu})

def ModProfesional(request):
    formu = NuevoAlumno()
    return render(request,'AppScholl/components/modprofesional.html',{'form':formu})