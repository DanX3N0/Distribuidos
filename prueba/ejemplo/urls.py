from django.urls import path
#con el punto recorre todo el directorio acutal
#from .views import index
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #esta ak reves el path pero tambien
    #se puede colocar al reves de como se ve
    #'saludo/<str:nombre>'
    path('<str:nombre>/saludo', views.saludo, name='saludo'),
]
