from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#en vistas debe recibir el parametro request
#vistas, modelos, templates, urls -> deben tener esos 4
#archivos como minimo
def index(request):
   #return HttpResponse("hola")
   return render(request, 'index.html')

def saludo(request, nombre):
   #return HttpResponse("hola : %s" %nombre)
   #render se posiciona en la carpeta templates
   diccionario = {'nombre':nombre, 'edad':25}
   return render(request, 'saludar.html', diccionario)

#
#<!--Imprime: {{ variable }}-->
#      <!--{% if condicion %}-->
#      <!--{% else %}-->
#      <!--{% endif %}-->
#      <!--{% while condicion %}-->
#      <!--{% endwhile %}-->
#      <!--{% n = 0 %}-->
#      <!--{{ n += 1 }}-->
#      <!--{% for i in vector %}-->
#      <!--   {{i}}-->
#      <!--{% endfor %}-->