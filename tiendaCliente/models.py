from django.db import models
from tenant_schemas.models import TenantMixin

class TiendaCliente(TenantMixin):
    nombre = models.CharField(max_length=100)
    en_prueba = models.BooleanField(default=False)
    creado_en = models.DateField(auto_now_add=True)
    auto_create_schema = True

    def __str__(self):
        return self.nombre