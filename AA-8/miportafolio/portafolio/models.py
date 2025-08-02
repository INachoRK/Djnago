from django.db import models

class ExperienciaLaboral(models.Model):
    cargo = models.CharField(max_length=100, help_text="Nombre del cargo desempeñado")
    empresa = models.CharField(max_length=100, help_text="Nombre de la empresa")
    fecha_inicio = models.DateField(help_text="Fecha de inicio")
    fecha_fin = models.DateField(help_text="Fecha de finalización")
    descripcion = models.TextField(help_text="Descripción de las funciones")

    def __str__(self):
        return f"{self.cargo} en {self.empresa}"

class Estudio(models.Model):
    institucion = models.CharField(max_length=100, help_text="Nombre de la institución educativa")
    titulo = models.CharField(max_length=100, help_text="Título obtenido")
    fecha_inicio = models.DateField(help_text="Fecha de inicio de estudios")
    fecha_fin = models.DateField(help_text="Fecha de finalización de estudios")

    def __str__(self):
        return f"{self.titulo} en {self.institucion}"

class Hobbie(models.Model):
    nombre = models.CharField(max_length=100, help_text="Nombre del hobbie o pasatiempo")
    descripcion = models.TextField(blank=True, help_text="Descripción breve (opcional)")

    def __str__(self):
        return self.nombre

