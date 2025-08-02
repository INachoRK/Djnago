from django.shortcuts import render, redirect, get_object_or_404
from .models import ExperienciaLaboral, Estudio, Hobbie
from .forms import ExperienciaLaboralForm, EstudioForm, HobbieForm

def experiencia_list(request):
    experiencias = ExperienciaLaboral.objects.all()
    return render(request, 'portafolio/experiencia_list.html', {'experiencias': experiencias})

def experiencia_create(request):
    if request.method == 'POST':
        form = ExperienciaLaboralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('experiencia_list')
    else:
        form = ExperienciaLaboralForm()
    return render(request, 'portafolio/experiencia_form.html', {'form': form})

def experiencia_update(request, pk):
    experiencia = get_object_or_404(ExperienciaLaboral, pk=pk)
    if request.method == 'POST':
        form = ExperienciaLaboralForm(request.POST, instance=experiencia)
        if form.is_valid():
            form.save()
            return redirect('experiencia_list')
    else:
        form = ExperienciaLaboralForm(instance=experiencia)
    return render(request, 'portafolio/experiencia_form.html', {'form': form})

def experiencia_delete(request, pk):
    experiencia = get_object_or_404(ExperienciaLaboral, pk=pk)
    if request.method == 'POST':
        experiencia.delete()
        return redirect('experiencia_list')
    return render(request, 'portafolio/experiencia_confirm_delete.html', {'experiencia': experiencia})

def estudio_list(request):
    estudios = Estudio.objects.all()
    return render(request, 'portafolio/estudio_list.html', {'estudios': estudios})

def estudio_create(request):
    if request.method == 'POST':
        form = EstudioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estudio_list')
    else:
        form = EstudioForm()
    return render(request, 'portafolio/estudio_form.html', {'form': form})

def estudio_update(request, pk):
    estudio = get_object_or_404(Estudio, pk=pk)
    if request.method == 'POST':
        form = EstudioForm(request.POST, instance=estudio)
        if form.is_valid():
            form.save()
            return redirect('estudio_list')
    else:
        form = EstudioForm(instance=estudio)
    return render(request, 'portafolio/estudio_form.html', {'form': form})

def estudio_delete(request, pk):
    estudio = get_object_or_404(Estudio, pk=pk)
    if request.method == 'POST':
        estudio.delete()
        return redirect('estudio_list')
    return render(request, 'portafolio/estudio_confirm_delete.html', {'estudio': estudio})

def hobbie_list(request):
    hobbies = Hobbie.objects.all()
    return render(request, 'portafolio/hobbie_list.html', {'hobbies': hobbies})

def hobbie_create(request):
    if request.method == 'POST':
        form = HobbieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hobbie_list')
    else:
        form = HobbieForm()
    return render(request, 'portafolio/hobbie_form.html', {'form': form})

def hobbie_update(request, pk):
    hobbie = get_object_or_404(Hobbie, pk=pk)
    if request.method == 'POST':
        form = HobbieForm(request.POST, instance=hobbie)
        if form.is_valid():
            form.save()
            return redirect('hobbie_list')
    else:
        form = HobbieForm(instance=hobbie)
    return render(request, 'portafolio/hobbie_form.html', {'form': form})

def hobbie_delete(request, pk):
    hobbie = get_object_or_404(Hobbie, pk=pk)
    if request.method == 'POST':
        hobbie.delete()
        return redirect('hobbie_list')
    return render(request, 'portafolio/hobbie_confirm_delete.html', {'hobbie': hobbie})
