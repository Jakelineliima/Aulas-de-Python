from django.shortcuts import render

from rest_framework import viewsets
from lavajato.models import Cliente, Veiculo
from lavajato.serializer import ClienteSerializer, VeiculoSerializer
class ClientesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
class VeiculosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os veiculos"""
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer