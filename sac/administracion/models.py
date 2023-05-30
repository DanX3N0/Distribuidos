from django.db import models

# Create your models here.
class Persona(models.Model):
    #se pude hacer uso de default como segundo parametro
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=30)
    ci = models.CharField(max_length=10, unique=True)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=8)
    correo = models.EmailField(max_length=100)
    fecha_nacimiento = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.apellidos} {self.nombre} {self.ci}"
    
    class Meta:
        ordering = ["apellidos", "nombre"]

class Cajera(models.Model):
    item = models.CharField(max_length=5, unique=True, help_text='Numero Item')
    fecha_ingreso = models.DateField()
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.item

class Socio(models.Model):
    numero = models.CharField(max_length=5, unique=True)
    fecha_ingreso = models.DateField()
    cuenta_ahorro = models.CharField(max_length= 13, unique=True)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.numero

class Oficial(models.Model):
    item = models.CharField(max_length=5, unique=True, help_text='Numero Item')
    fecha_ingreso = models.DateField()
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.item

