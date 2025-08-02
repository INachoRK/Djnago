from django.shortcuts import render, redirect, get_object_or_404
from .models import Habilidad, Estudio, Experiencia, Proyecto, Hobby, Contacto
from .forms import HabilidadForm, EstudioForm, ExperienciaForm, ProyectoForm, HobbyForm, ContactoForm

# LANDING PAGE
def index(request):
    return render(request, 'core/index.html')

# HABILIDADES

def lista_habilidades(request):
    habilidades = Habilidad.objects.all()
    return render(request, 'core/habilidades/lista.html', {'habilidades': habilidades})

def crear_habilidad(request):
    if request.method == 'POST':
        form = HabilidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_habilidades')
    else:
        form = HabilidadForm()
    return render(request, 'core/habilidades/formulario.html', {'form': form})

def editar_habilidad(request, id):
    habilidad = get_object_or_404(Habilidad, id=id)
    if request.method == 'POST':
        form = HabilidadForm(request.POST, instance=habilidad)
        if form.is_valid():
            form.save()
            return redirect('lista_habilidades')
    else:
        form = HabilidadForm(instance=habilidad)
    return render(request, 'core/habilidades/formulario.html', {'form': form})

def eliminar_habilidad(request, id):
    habilidad = get_object_or_404(Habilidad, id=id)
    if request.method == 'POST':
        habilidad.delete()
        return redirect('lista_habilidades')
    return render(request, 'core/habilidades/eliminar.html', {'habilidad': habilidad})

# ESTUDIOS

def lista_estudios(request):
    estudios = Estudio.objects.all()
    return render(request, 'core/estudios/lista.html', {'estudios': estudios})

def crear_estudio(request):
    if request.method == 'POST':
        form = EstudioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudios')
    else:
        form = EstudioForm()
    return render(request, 'core/estudios/formulario.html', {'form': form})

def editar_estudio(request, id):
    estudio = get_object_or_404(Estudio, id=id)
    if request.method == 'POST':
        form = EstudioForm(request.POST, instance=estudio)
        if form.is_valid():
            form.save()
            return redirect('lista_estudios')
    else:
        form = EstudioForm(instance=estudio)
    return render(request, 'core/estudios/formulario.html', {'form': form})

def eliminar_estudio(request, id):
    estudio = get_object_or_404(Estudio, id=id)
    if request.method == 'POST':
        estudio.delete()
        return redirect('lista_estudios')
    return render(request, 'core/estudios/eliminar.html', {'estudio': estudio})

# EXPERIENCIA

def lista_experiencia(request):
    experiencias = Experiencia.objects.all()
    return render(request, 'core/experiencia/lista.html', {'experiencias': experiencias})

def crear_experiencia(request):
    if request.method == 'POST':
        form = ExperienciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_experiencia')
    else:
        form = ExperienciaForm()
    return render(request, 'core/experiencia/formulario.html', {'form': form})

def editar_experiencia(request, id):
    experiencia = get_object_or_404(Experiencia, id=id)
    if request.method == 'POST':
        form = ExperienciaForm(request.POST, instance=experiencia)
        if form.is_valid():
            form.save()
            return redirect('lista_experiencia')
    else:
        form = ExperienciaForm(instance=experiencia)
    return render(request, 'core/experiencia/formulario.html', {'form': form})

def eliminar_experiencia(request, id):
    experiencia = get_object_or_404(Experiencia, id=id)
    if request.method == 'POST':
        experiencia.delete()
        return redirect('lista_experiencia')
    return render(request, 'core/experiencia/eliminar.html', {'experiencia': experiencia})

# PROYECTOS

def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'core/proyectos/lista.html', {'proyectos': proyectos})

def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'core/proyectos/formulario.html', {'form': form})

def editar_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'core/proyectos/formulario.html', {'form': form})

def eliminar_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('lista_proyectos')
    return render(request, 'core/proyectos/eliminar.html', {'proyecto': proyecto})

# HOBBIES

def lista_hobbies(request):
    hobbies = Hobby.objects.all()
    return render(request, 'core/hobbies/lista.html', {'hobbies': hobbies})

def crear_hobby(request):
    if request.method == 'POST':
        form = HobbyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_hobbies')
    else:
        form = HobbyForm()
    return render(request, 'core/hobbies/formulario.html', {'form': form})

def editar_hobby(request, id):
    hobby = get_object_or_404(Hobby, id=id)
    if request.method == 'POST':
        form = HobbyForm(request.POST, instance=hobby)
        if form.is_valid():
            form.save()
            return redirect('lista_hobbies')
    else:
        form = HobbyForm(instance=hobby)
    return render(request, 'core/hobbies/formulario.html', {'form': form})

def eliminar_hobby(request, id):
    hobby = get_object_or_404(Hobby, id=id)
    if request.method == 'POST':
        hobby.delete()
        return redirect('lista_hobbies')
    return render(request, 'core/hobbies/eliminar.html', {'hobby': hobby})

# CONTACTO

def contacto(request):
    enviado = False
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            enviado = True
    else:
        form = ContactoForm()
    return render(request, 'core/contacto.html', {'form': form, 'enviado': enviado})