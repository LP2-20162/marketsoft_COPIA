from uuid import uuid4
from django.db import models
from .producto import Producto
from .cliente import Cliente
from django.db.models import signals
from .compra import TimeStampModel


class Cabecera_Venta(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    ruc = models.CharField(max_length=10, unique=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.ruc


class todo_item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    list_id = models.ForeignKey(Cabecera_Venta)
    producto = models.ForeignKey(Producto)
    cantidad = models.IntegerField()


def update_stock(sender, instance, **kwargs):
    instance.producto.stock -= instance.cantidad
    instance.producto.save()

# register the signal
signals.post_save.connect(update_stock, sender=todo_item,
                          dispatch_uid="update_stock_count")
