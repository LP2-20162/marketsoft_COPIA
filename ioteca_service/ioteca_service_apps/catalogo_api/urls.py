from django.conf.urls import url, include
from rest_framework import routers

from .distribuidor_view import DistribuidorViewSet
from .cliente_view import ClienteViewSet
from .empresa_view import EmpresaViewSet
from .producto_view import ProductoViewSet
from .cabecera_view import CompraViewSet

router = routers.DefaultRouter()

router.register(r'discribuidor', DistribuidorViewSet, 'distribuidor-view')
router.register(r'cliente', ClienteViewSet, 'cliente-view')
router.register(r'empresa', EmpresaViewSet, 'empresa-view')
router.register(r'producto', ProductoViewSet, 'producto-view')
router.register(r'cabecera', CompraViewSet, 'cabecera-view')

urlpatterns = [

    url(r'^', include(router.urls)),

]
