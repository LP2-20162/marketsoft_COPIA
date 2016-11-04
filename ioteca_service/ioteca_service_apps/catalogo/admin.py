from django.contrib import admin
from .models.producto import Presentacion
from .models.cliente import Cliente
from .models.producto import Producto
from .models.distribuidor import Distribuidor
from .models.empresa import Empresa
from .models.compra import DetalleCompra
from .models.compra import Cabecera
from .models.venta import todo_item, Cabecera_Venta
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
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('lote', 'presentancion', 'nombre', 'descripcion', 'fecha_expiracion',
                    'fecha_produccion',  'precio_Compra', 'precio_venta', 'stock')
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


class producto_compraInline(admin.TabularInline):
    model = DetalleCompra


class compraAdmin(admin.ModelAdmin):
    inlines = (producto_compraInline,)

admin.site.register(Cabecera, compraAdmin)


class producto_ventaInline(admin.TabularInline):
    model = todo_item


class Detalle_VentaAdmin(admin.ModelAdmin):
    inlines = (producto_ventaInline,)

admin.site.register(Cabecera_Venta, Detalle_VentaAdmin)
