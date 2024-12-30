from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView,CreateView,TemplateView,UpdateView
from AppScholl.models import Profesional,Alumno,Asignatura
from AppScholl.forms import NuevoCurso,InicioSesion,NuevaCarrera,NuevoAlumno,NuevoProfesional,Buscar



class InicioView(TemplateView):
    template_name = 'AppScholl/inicio.html'   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profesionales'] = Profesional.objects.all() 
        context['cursos'] = Asignatura.objects.filter(tipo='curso')  
        context['carreras'] = Asignatura.objects.filter(tipo='carrera') 
        return context

class CursoListView(ListView):
    model = Asignatura
    template_name = 'AppScholl/cursos.html'
    context_object_name = 'cursos' 
    def get_queryset(self):  
        query = self.request.GET.get('buscador', '')
        filtro = self.request.GET.get('filtro', '')
        if filtro:
            return Asignatura.objects.filter(tipo='curso', categoria__icontains=filtro)
        elif query:
            return Asignatura.objects.filter(tipo='curso', nombre__icontains=query)
        else:
            return Asignatura.objects.filter(tipo='curso')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['buscar'] = Buscar(self.request.GET)
        context['query'] = self.request.GET.get('buscador', '')
        context['filtro'] = self.request.GET.get('filtro', '')
        return context
    def post(self, request, *args, **kwargs):
        if 'eliminar' in request.POST:
            curso_nombre = request.POST.get('curso_nombre')
            if curso_nombre:
                curso = Asignatura.objects.filter(nombre=curso_nombre).first()
                if curso:
                    curso.delete()  
        return redirect('Cursos')

class CarreraListView(ListView):
    model = Asignatura
    template_name = 'AppScholl/carreras.html'
    context_object_name = 'carreras'  

    def get_queryset(self):
        query = self.request.GET.get('buscador', '')
        filtro = self.request.GET.get('filtro', '')
        if filtro:
            return Asignatura.objects.filter(tipo='carrera', categoria__icontains=filtro)
        elif query:
            return Asignatura.objects.filter(tipo='carrera', nombre__icontains=query)
        else:
            return Asignatura.objects.filter(tipo='carrera')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['buscar'] = Buscar(self.request.GET)  
        context['query'] = self.request.GET.get('buscador', '')
        context['filtro'] = self.request.GET.get('filtro', '')
        return context

    def post(self, request, *args, **kwargs):
        if 'eliminar' in request.POST:
            carrera_nombre = request.POST.get('carrera_nombre')
            if carrera_nombre:
                carrera = Asignatura.objects.filter(nombre=carrera_nombre).first()
                if carrera:
                    carrera.delete()  
        return redirect('Carreras')



class AlumnoListView(ListView):
    model = Alumno
    template_name = 'AppScholl/alumnos.html'
    context_object_name = 'alumnos'
    def get_queryset(self):
        query = self.request.GET.get('buscador', '')
        if query:
            if query.isdigit():
                return Alumno.objects.filter(documento__icontains=query)
            else:
                return Alumno.objects.filter(apellido__icontains=query)
        else:
            return Alumno.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['buscar'] = Buscar(self.request.GET)
        context['query'] = self.request.GET.get('buscador', '')
        return context
    def post(self, request, *args, **kwargs):
        if 'eliminar' in request.POST:
            alumno_documento = request.POST.get('alumno_documento')
            if alumno_documento:
                alumno = Alumno.objects.filter(documento=alumno_documento).first()
                if alumno:
                    alumno.delete()
        return redirect('Alumnos')
    
    
    
    
class ProfesionalListView(ListView):
    model = Profesional
    template_name = 'AppScholl/profesionales.html'
    context_object_name = 'profesionales'

    def get_queryset(self):
        query = self.request.GET.get('buscador', '')
        filtro = self.request.GET.get('filtro', '')
        
        if filtro:
            return Profesional.objects.filter(rol__icontains=filtro)
        elif query:
            return Profesional.objects.filter(nombre__icontains=query)
        else:
            return Profesional.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['buscar'] = Buscar(self.request.GET)
        context['query'] = self.request.GET.get('buscador', '')
        context['filtro'] = self.request.GET.get('filtro', '')
        return context

    def post(self, request, *args, **kwargs):
        if 'eliminar' in request.POST:
            profesional_documento = request.POST.get('profesional_documento')
            if profesional_documento:
                profesional = Profesional.objects.filter(documento=profesional_documento).first()
                if profesional:
                    profesional.delete()
        return redirect('Profesionales')



def login(request):
    log = InicioSesion
    return render(request,'AppScholl/login.html',{'login':log})




# vistas agregar
class AddCursoView(CreateView):
    model = Asignatura
    form_class = NuevoCurso
    template_name = 'AppScholl/components/addcurso.html'
    success_url = '/cursos/'

    def form_valid(self, form):
        form.instance.tipo = 'curso'
        return super().form_valid(form)

class AddCarreraView(CreateView):
    model = Asignatura
    form_class = NuevaCarrera
    template_name = 'AppScholl/components/addcarrera.html'
    success_url = '/carreras/'

    def form_valid(self, form):
        form.instance.tipo = 'carrera'
        return super().form_valid(form)

class AddAlumnoView(CreateView):
    model = Alumno
    form_class = NuevoAlumno
    template_name = 'AppScholl/components/addalumno.html'
    success_url = '/alumnos/'

class AddProfesionalView(CreateView):
    model = Profesional
    form_class = NuevoProfesional
    template_name = 'AppScholl/components/addprofesional.html'
    success_url = '/profesionales/'

class ModCursoView(UpdateView):
    model = Asignatura
    form_class = NuevoCurso
    template_name = 'AppScholl/components/modcurso.html'
    success_url = '/cursos/'
    context_object_name = 'curso'

    def get_object(self, queryset=None):
        return get_object_or_404(Asignatura, nombre=self.kwargs['curso_nombre'])

class ModCarreraView(UpdateView):
    model = Asignatura
    form_class = NuevaCarrera
    template_name = 'AppScholl/components/modcarrera.html'
    success_url = '/carreras/'
    context_object_name = 'carrera'

    def get_object(self, queryset=None):
        return get_object_or_404(Asignatura, nombre=self.kwargs['carrera_nombre'])

class ModAlumnoView(UpdateView):
    model = Alumno
    form_class = NuevoAlumno
    template_name = 'AppScholl/components/modalumno.html'
    success_url = '/alumnos/'
    context_object_name = 'alumno'

    def get_object(self, queryset=None):
        return get_object_or_404(Alumno, documento=self.kwargs['alumno_documento'])

class ModProfesionalView(UpdateView):
    model = Profesional
    form_class = NuevoProfesional
    template_name = 'AppScholl/components/modprofesional.html'
    success_url = '/profesionales/'
    context_object_name = 'profesional'

    def get_object(self, queryset=None):
        return get_object_or_404(Profesional, documento=self.kwargs['profesional_documento'])