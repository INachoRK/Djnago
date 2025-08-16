from django.urls import path
from .views import (
    TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView
)

urlpatterns = [
    path('',              TaskListView.as_view(),   name='tasks_list'),
    path('crear/',        TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/edit/',TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/del/', TaskDeleteView.as_view(), name='task_delete'),
]