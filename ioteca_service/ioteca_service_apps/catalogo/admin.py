from django.contrib import admin
from .models.producto import Presentacion
from .models.cliente import Cliente
from .models.producto import Producto
from .models.distribuidor import Distribuidor
from .models.empresa import Empresa
# Register your models here.


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'dni', 'direccion')
    search_fields = ('dni', 'nombre', 'apellidos')
    list_per_page = 3


@admin.register(Presentacion)
class PresentacionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_per_page = 3


@admin.register(Producto)
class MedicamentosAdmin(admin.ModelAdmin):
    list_display = ('lote', 'presentacion', 'nombre', 'descripcion', 'fecha_expiracion',
                    'fecha_produccion', 'tipo', 'precio_Compra', 'precio_venta', 'stock')
    search_fields = ('nombre', 'descripcion')
    list_per_page = 3


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('ruc', 'nombre')
    list_per_page = 3


@admin.register(Distribuidor)
class DistribuidorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ruc')
    search_fields = ('codigo', 'nombre')
