from rest_framework import serializers, viewsets
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce

from ioteca_service_apps.catalogo.models.compra import DetalleCompra


class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCompra
        # fields = ('url', 'username', 'email', 'is_staff')


class CompraViewSet(viewsets.ModelViewSet):
    queryset = DetalleCompra.objects.all()
    serializer_class = CompraSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        queryall = (Q(codigo__icontains=query),
                    Q(nombre__icontains=query))
        queryset = self.queryset.filter(reduce(OR, queryall))
        return queryset
