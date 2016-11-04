from rest_framework import serializers, viewsets
from ioteca_service_apps.catalogo.models.empresa import Empresa


class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
