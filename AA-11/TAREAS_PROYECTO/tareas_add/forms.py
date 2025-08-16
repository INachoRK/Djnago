from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descripción'
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Fecha de vencimiento'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Estado'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Categoría'
            }),
        }
