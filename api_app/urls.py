from django.urls import path
from .views import (
    PersonaDetail, PersonaList, PersonaByDocumento, ActualizarPersona, TareaList, CrearTarea, TareaDetail, TareaByFecha, TareaByRangoFechas, TareaByPersona
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
    path('tareas/fecha/<str:fecha>/', TareaByFecha.as_view(), name='tarea-by-fecha'),
    path('tareas/rango/<str:fecha_inicio>/<str:fecha_fin>/', TareaByRangoFechas.as_view(), name='tarea-by-rango-fechas'),
    path('tareas/persona/<str:documento>/', TareaByPersona.as_view(), name='tarea-by-persona'),
]
