"""
prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .views import saludar, datos, index, Cuadrado


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('saludar/',saludar, name="saludar"),
    path('dato/<str:nombres>/<int:edad>', datos, name="datos"),
    path('cuadrado/<int:lado>', Cuadrado.as_view(), name="cuadrado"),
    #con include agrega la carpeta de la otra app
    #los params son el nombre de la carpeta y el 
    #archivo urls / se debe importar include
    path('ejemplo/', include('ejemplo.urls'), name='ejemplo'),
]
