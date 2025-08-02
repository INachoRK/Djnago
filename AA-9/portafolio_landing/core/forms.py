from django import forms
from .models import Habilidad, Estudio, Experiencia, Proyecto, Hobby, Contacto

class HabilidadForm(forms.ModelForm):
    class Meta:
        model = Habilidad
        fields = '__all__'

class EstudioForm(forms.ModelForm):
    class Meta:
        model = Estudio
        fields = '__all__'

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = '__all__'

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = '__all__'

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'correo', 'mensaje']
