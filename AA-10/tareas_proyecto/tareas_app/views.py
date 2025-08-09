from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Tarea, Categoria

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    tareas = Tarea.objects.filter(usuario=request.user)
    return render(request, 'dashboard.html', {'tareas': tareas})

@login_required
def dashboard(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '').strip()
        descripcion = request.POST.get('descripcion', '').strip()
        categoria_id = request.POST.get('categoria')
        completada = request.POST.get('completada') == 'on'

        if titulo and categoria_id:
            categoria = get_object_or_404(Categoria, id=categoria_id)
            Tarea.objects.create(
                titulo=titulo,
                descripcion=descripcion,
                completada=completada,
                categoria=categoria,
                usuario=request.user
            )
            return redirect('dashboard')

    tareas = Tarea.objects.filter(usuario=request.user).select_related('categoria')
    categorias = Categoria.objects.all().order_by('nombre')
    return render(request, 'dashboard.html', {'tareas': tareas, 'categorias': categorias})
