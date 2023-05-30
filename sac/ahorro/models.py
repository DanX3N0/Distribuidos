from django.db import models
from administracion.models import Socio, Cajera

# Create your models here.
class Ahorro(models.Model):
   debito = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
   credito = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
   saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
   fecha = models.DateTimeField(verbose_name="Fecha de Operacion")
   socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
   cajera = models.ForeignKey(Cajera, on_delete=models.CASCADE)



