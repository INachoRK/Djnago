from django.urls import path
from . import views

urlpatterns = [
    path('experiencias/', views.experiencia_list, name='experiencia_list'),
    path('experiencias/nueva/', views.experiencia_create, name='experiencia_create'),
    path('experiencias/editar/<int:pk>/', views.experiencia_update, name='experiencia_update'),
    path('experiencias/eliminar/<int:pk>/', views.experiencia_delete, name='experiencia_delete'),

    path('estudios/', views.estudio_list, name='estudio_list'),
    path('estudios/nuevo/', views.estudio_create, name='estudio_create'),
    path('estudios/editar/<int:pk>/', views.estudio_update, name='estudio_update'),
    path('estudios/eliminar/<int:pk>/', views.estudio_delete, name='estudio_delete'),

    path('hobbies/', views.hobbie_list, name='hobbie_list'),
    path('hobbies/nuevo/', views.hobbie_create, name='hobbie_create'),
    path('hobbies/editar/<int:pk>/', views.hobbie_update, name='hobbie_update'),
    path('hobbies/eliminar/<int:pk>/', views.hobbie_delete, name='hobbie_delete'),
]
