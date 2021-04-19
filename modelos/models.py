from django.db import models
from datetime import date
from tenant_schemas.models import TenantMixin



class Trabajos(models.Model):
    
    fecha    = models.DateTimeField(auto_now_add = True)
    trabajo  = models.CharField(max_length=80, null=False)
    nombre   = models.CharField(max_length=80, null=False)
    telefono = models.BigIntegerField(null=False)
    precio   = models.DecimalField(max_digits=7, decimal_places=2, null=False)
    empleado = models.CharField(max_length=40, null=False)
    tarjeta  = models.BooleanField(default=None)
    
    def clean(self):
        self.trabajo  = self.trabajo.upper()
        self.nombre   = self.nombre.upper()
        self.empleado = self.empleado.upper()

    def __str__(self):
        return self.nombre   
           

class Stock(models.Model):

    fecha      = models.DateTimeField(auto_now_add = True)
    producto   = models.CharField(max_length=80, null=False)
    cantidad   = models.IntegerField(null=False)
    accion     = models.CharField(max_length=20)
    trabajo_id = models.ForeignKey(Trabajos, on_delete=models.CASCADE, null=True)

    def clean(self):
        self.producto = self.producto.upper()

    def __str__(self):
        return self.producto


class Turnos(models.Model):

    fecha    = models.DateTimeField(unique=True, null=False)
    telefono = models.BigIntegerField(null=True, blank=True)
    cliente  = models.CharField(max_length=40, null=False)
    empleado = models.CharField(max_length=40, null=False)

    def clean(self):
        self.cliente  = self.cliente.upper()
        self.empleado = self.empleado.upper()

    def __str__(self):
        return self.cliente    


class Empleados(models.Model):

    fecha      = models.DateField(default=date.today, null=False)
    nombre     = models.CharField(max_length=40, null=False)
    telefono   = models.BigIntegerField(null=True, blank=True)
    direccion  = models.CharField(max_length=60, null=False)
    

    def clean(self):
        self.nombre  = self.nombre.upper()
        self.direccion = self.direccion.upper()

    def __str__(self):
        return self.nombre


          