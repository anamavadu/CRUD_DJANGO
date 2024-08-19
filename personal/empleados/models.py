from django.db import models
from datetime import date

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.TextField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    ingreso = models.DateField(default=date.today)
    imagen = models.ImageField(upload_to='empleados/', null=True, blank=True)

    def __str__(self):
        return self.nombre