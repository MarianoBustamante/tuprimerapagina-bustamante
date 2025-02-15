from django.urls import path
from . import views

urlpatterns = [
    path('', views.agregar_entrada, name='inicio'),  # Redirige a la vista de "Nueva Entrada"
    path('nuevo_escritor/', views.agregar_escritor, name='nuevo_escritor'),
    path('nuevo_tema/', views.agregar_tema, name='nuevo_tema'),
    path('nueva_entrada/', views.agregar_entrada, name='nueva_entrada'),
    path('buscar/', views.buscar_entrada, name='buscar_entrada'),
    path('entrada/<int:pk>/', views.ver_entrada, name='ver_entrada'),
]
