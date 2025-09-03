from django.urls import path
from .views import (
    PersonaDetail, PersonaList, PersonaByDocumento, ActualizarPersona, TareaList, CrearTarea, TareaDetail
)



urlpatterns = [
    # Personas
    path('personas/', PersonaList.as_view(), name='persona-list'),
    path('personas/crear/', PersonaList.as_view(), name='persona-crear'),
    path('personas/actualizar/<int:pk>/', ActualizarPersona.as_view(), name='persona-actualizar'),
    path('personas/documento/<str:documento>/', PersonaByDocumento.as_view(), name='persona-por-documento'),
    path('personas/<int:pk>/', PersonaDetail.as_view(), name='persona-detail'),
    # Tareas
    path('tareas/', TareaList.as_view(), name='tarea-list'),
    path('tareas/crear/', CrearTarea.as_view(), name='tarea-crear'),
    path('tareas/<int:pk>/', TareaDetail.as_view(), name='tarea-detail'),
]
