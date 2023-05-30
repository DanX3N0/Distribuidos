from django.shortcuts import render, HttpResponse ,redirect
from .models import Persona

# Create your views here.
def index(request):
   personas = Persona.objects.all()
   '''
   SELECT *
   FROM administracion_persona
   '''
   #return HttpResponse(personas)
   return render(request, 'personas/index.html', {'personas': personas})

def nuevo(request):
   if request.method == 'GET':
      return render(request, 'personas/nuevo.html')
   else:
      data = request.POST
      persona = Persona(
         nombre = data.get('nombres'),
         apellidos = data.get('apellidos'),
         direccion = data.get('direccion'),
         telefono = data.get('telefono'),
         ci = data.get('ci'),
         fecha_nacimiento = data.get('fecha_nacimiento'),         
      )
      persona.save()
      #return HttpResponse(persona)
      return redirect('persona_index')

'''
INSERT INTO administracion values('nombre', 'apellido')
'''