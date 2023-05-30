from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='persona_index'),
    path('nuevoPersona', views.nuevo, name='persona_nuevo'),
]