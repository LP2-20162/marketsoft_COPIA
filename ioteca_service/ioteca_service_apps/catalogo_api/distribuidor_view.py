from rest_framework import serializers, viewsets
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce

from ioteca_service_apps.catalogo.models.distribuidor import Distribuidor


class DistribuidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distribuidor
        # fields = ('url', 'username', 'email', 'is_staff')


class DistribuidorViewSet(viewsets.ModelViewSet):
    queryset = Distribuidor.objects.all()
    serializer_class = DistribuidorSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        queryall = (Q(codigo__icontains=query),
                    Q(nombre__icontains=query))
        queryset = self.queryset.filter(reduce(OR, queryall))
        return queryset
