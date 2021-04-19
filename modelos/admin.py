from django.contrib import admin

# Register your models here.
from modelos.models import Trabajos, Stock, Turnos, Empleados
from tiendaCliente.models import TiendaCliente

admin.site.register(Trabajos)
admin.site.register(Stock)
admin.site.register(Turnos)
admin.site.register(Empleados)
admin.site.register(TiendaCliente)