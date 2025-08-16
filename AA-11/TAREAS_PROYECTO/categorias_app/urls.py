from django.urls import path
from .views import (
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
)

urlpatterns = [
    path('',              CategoryListView.as_view(),  name='categories_list'),
    path('crear/',        CategoryCreateView.as_view(), name='category_create'),
    path('<int:pk>/edit/',CategoryUpdateView.as_view(), name='category_update'),
    path('<int:pk>/del/', CategoryDeleteView.as_view(), name='category_delete'),
]