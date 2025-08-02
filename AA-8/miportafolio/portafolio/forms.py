from django import forms
from .models import ExperienciaLaboral, Estudio, Hobbie

class ExperienciaLaboralForm(forms.ModelForm):
    class Meta:
        model = ExperienciaLaboral
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

class EstudioForm(forms.ModelForm):
    class Meta:
        model = Estudio
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

class HobbieForm(forms.ModelForm):
    class Meta:
        model = Hobbie
        fields = '__all__'
