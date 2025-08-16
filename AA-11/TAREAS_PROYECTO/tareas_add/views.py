from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from categorias_app.models import Category

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        role = getattr(self.request.user.profile, 'role', 'USER')
        qs = Task.objects.select_related('category', 'owner')
        return qs if role == 'ADMIN' else qs.filter(owner=self.request.user)

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'status', 'category']
    template_name = 'tasks/form.html'
    success_url = reverse_lazy('tasks_list')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        # limitar categorías a las del usuario (a menos que sea admin)
        role = getattr(self.request.user.profile, 'role', 'USER')
        if role != 'ADMIN':
            form.fields['category'].queryset = Category.objects.filter(owner=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'status', 'category']
    template_name = 'tasks/form.html'
    success_url = reverse_lazy('tasks_list')

    def get_queryset(self):
        role = getattr(self.request.user.profile, 'role', 'USER')
        qs = Task.objects.all()
        return qs if role == 'ADMIN' else qs.filter(owner=self.request.user)

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/confirm_delete.html'
    success_url = reverse_lazy('tasks_list')

    def get_queryset(self):
        role = getattr(self.request.user.profile, 'role', 'USER')
        qs = Task.objects.all()
        return qs if role == 'ADMIN' else qs.filter(owner=self.request.user)
