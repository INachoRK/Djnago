from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name        = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    owner       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']

    def __str__(self):
        return self.name
