from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),

    # Habilidades
    path('habilidades/', views.lista_habilidades, name='lista_habilidades'),
    path('habilidades/crear/', views.crear_habilidad, name='crear_habilidad'),
    path('habilidades/editar/<int:id>/', views.editar_habilidad, name='editar_habilidad'),
    path('habilidades/eliminar/<int:id>/', views.eliminar_habilidad, name='eliminar_habilidad'),

    # Estudios
    path('estudios/', views.lista_estudios, name='lista_estudios'),
    path('estudios/crear/', views.crear_estudio, name='crear_estudio'),
    path('estudios/editar/<int:id>/', views.editar_estudio, name='editar_estudio'),
    path('estudios/eliminar/<int:id>/', views.eliminar_estudio, name='eliminar_estudio'),

    # Experiencia
    path('experiencia/', views.lista_experiencia, name='lista_experiencia'),
    path('experiencia/crear/', views.crear_experiencia, name='crear_experiencia'),
    path('experiencia/editar/<int:id>/', views.editar_experiencia, name='editar_experiencia'),
    path('experiencia/eliminar/<int:id>/', views.eliminar_experiencia, name='eliminar_experiencia'),

    # Proyectos
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),
    path('proyectos/crear/', views.crear_proyecto, name='crear_proyecto'),
    path('proyectos/editar/<int:id>/', views.editar_proyecto, name='editar_proyecto'),
    path('proyectos/eliminar/<int:id>/', views.eliminar_proyecto, name='eliminar_proyecto'),

    # Hobbies
    path('hobbies/', views.lista_hobbies, name='lista_hobbies'),
    path('hobbies/crear/', views.crear_hobby, name='crear_hobby'),
    path('hobbies/editar/<int:id>/', views.editar_hobby, name='editar_hobby'),
    path('hobbies/eliminar/<int:id>/', views.eliminar_hobby, name='eliminar_hobby'),

    # Contacto
    path('contacto/', views.contacto, name='contacto'),
]
