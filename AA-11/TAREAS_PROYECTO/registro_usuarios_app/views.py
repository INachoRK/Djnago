from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from tareas_add.models import Task
from categorias_app.models import Category

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    role = getattr(request.user.profile, 'role', 'USER')

    if role == 'ADMIN':
        tasks_qs = Task.objects.select_related('category', 'owner')
        cats_qs  = Category.objects.select_related('owner')
    else:
        tasks_qs = Task.objects.filter(owner=request.user).select_related('category', 'owner')
        cats_qs  = Category.objects.filter(owner=request.user).select_related('owner')

    context = {
        'tasks_count': tasks_qs.count(),
        'cats_count': cats_qs.count(),
        'latest_tasks': tasks_qs[:5],
        'latest_cats': cats_qs[:5],
        'role': role
    }
    return render(request, 'dashboard.html', context)
