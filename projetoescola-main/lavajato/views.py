from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from lavajato.models import Veiculo, Cliente, Revisao
from lavajato.serializer import VeiculoSerializer, ClienteSerializer, RevisaoSerializer, ListaRevisaoClienteSerializer, ListaClientesRevisaoSerializer

from django.http import JsonResponse

class ClientesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class VeiculosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class RevisaoViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matriculas"""
    queryset = Revisao.objects.all()
    serializer_class = RevisaoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaRevisaoClienteSerializer(generics.ListAPIView):
    """Exibindo as matriculas de um aluno"""
    def get_queryset(self):
        queryset = Revisao.objects.filter(cliente_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaRevisaoClienteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaClientesRevisaoSerializer(generics.ListAPIView):
    """Exibindo alunos matriculados em um curso"""
    def get_queryset(self):
        queryset = Revisao.objects.filter(veiculo_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaClientesRevisaoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]