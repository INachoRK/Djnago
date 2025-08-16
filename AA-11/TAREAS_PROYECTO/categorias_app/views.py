from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Category

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'categories/list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        role = getattr(self.request.user.profile, 'role', 'USER')
        qs = Category.objects.all() if role == 'ADMIN' else Category.objects.filter(owner=self.request.user)
        return qs.order_by('name')

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'categories/form.html'
    success_url = reverse_lazy('categories_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'categories/form.html'
    success_url = reverse_lazy('categories_list')

    def get_queryset(self):
        role = getattr(self.request.user.profile, 'role', 'USER')
        return Category.objects.all() if role == 'ADMIN' else Category.objects.filter(owner=self.request.user)

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'categories/confirm_delete.html'
    success_url = reverse_lazy('categories_list')

    def get_queryset(self):
        role = getattr(self.request.user.profile, 'role', 'USER')
        return Category.objects.all() if role == 'ADMIN' else Category.objects.filter(owner=self.request.user)
