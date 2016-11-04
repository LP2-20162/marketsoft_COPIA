from uuid import uuid4
from django.db import models

import datetime
# Create your models here.

TAX_VALUE = 0.18

# Create your models here.


class Presentacion(models.Model):
    #codigo = models.CharField(max_length=10, unique=True)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=60)

    def __unicode__(self):
        return u'%s' % (self.nombre)


class Producto(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    TIPO = (
        ('generico', 'Generico'),
        ('comercial', 'Comercial'),
    )
    lote = models.CharField(max_length=10, unique=True, default=0)
    presentancion = models.ForeignKey(Presentacion)
    nombre = models.CharField(max_length=200, unique=True)
    sanitario = models.CharField(max_length=200)
    fecha_expiracion = models.DateField()
    fecha_produccion = models.DateField()
    descripcion = models.TextField(max_length=400)
    precio_Compra = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.00)
    precio_venta = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.00)
    stock = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.nombre

    def preeciototal(self):
        precio_total = self.precio_compra * self.stock
        return precio_total

    def estadoproducto(self):
        hoy = datetime.date.today()
        dias = (self.fecha_expiracion - hoy).days
        return dias

    def incrementarlote(self, *args, **kwargs):
        if self.lote == 0:
            self.lote += 1
            self.store.save()
        super(Producto, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.precio_venta:
            self.igv = round(float(self.precio_venta) * TAX_VALUE, 3)
            super(Producto, self).save(*args, **kwargs)
        else:
            self.igv = 0
            super(Producto, self).save(*args, **kwargs)
