from django.db import models

# HABILIDAD
class Habilidad(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=[('Técnica', 'Técnica'), ('Blanda', 'Blanda')])
    nivel = models.CharField(max_length=20, choices=[('Junior', 'Junior'), ('Semi-Senior', 'Semi-Senior'), ('Senior', 'Senior')])

    def __str__(self):
        return self.nombre

# ESTUDIO
class Estudio(models.Model):
    institucion = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    en_curso = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

# EXPERIENCIA
class Experiencia(models.Model):
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    actualmente = models.BooleanField(default=False)

    def __str__(self):
        return self.cargo

# PROYECTO
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    enlace = models.URLField(blank=True)

    def __str__(self):
        return self.nombre

# HOBBY
class Hobby(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

# CONTACTO
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.correo}"
