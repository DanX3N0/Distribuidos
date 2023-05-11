from django.http import HttpResponse
from datetime import datetime
from django.views import View

def saludar(request):
    return HttpResponse("vistas")

def index(request):
    fecha = datetime.now()
    return HttpResponse("index " + fecha.strftime('%d/%m/%Y, %H:%M:%S'))
    
def datos(request, nombres, edad):
    return HttpResponse("hola " + nombres + " tienes " + str(edad))

# view sin modelos
# detailviw, listview
class Cuadrado(View):
   def get(self, request, lado):
       area = lado * lado
       return HttpResponse("Area: " + str(area))

   def post(self, request, lado):
       return HttpResponse("Llamada a traves de POST.")

"""
<form action="url" name "nombre" method="post">
"""
