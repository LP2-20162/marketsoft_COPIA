from uuid import uuid4
from django.db import models


class Empresa(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    ruc = models.CharField(max_length=10)
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre
# agregar direccion
