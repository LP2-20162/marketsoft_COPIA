from rest_framework import serializers, viewsets
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce

from ioteca_service_apps.catalogo.models.venta import Cabecera_Venta


class VentaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cabecera_Venta
        # fields = ('url', 'username', 'email', 'is_staff')


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Cabecera_Venta.objects.all()
    serializer_class = VentaSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        queryall = (Q(codigo__icontains=query),
                    Q(nombre__icontains=query))
        queryset = self.queryset.filter(reduce(OR, queryall))
        return queryset
