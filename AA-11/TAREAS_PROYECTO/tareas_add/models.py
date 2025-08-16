from django.db import models
from django.contrib.auth.models import User
from categorias_app.models import Category

class Task(models.Model):
    class Status(models.TextChoices):
        PENDIENTE     = 'PEN', 'Pendiente'
        EN_PROGRESO   = 'PRO', 'En progreso'
        COMPLETADA    = 'COM', 'Completada'

    title       = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    due_date    = models.DateField(null=True, blank=True)
    status      = models.CharField(max_length=3, choices=Status.choices, default=Status.PENDIENTE)
    category    = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='tasks')
    owner       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
