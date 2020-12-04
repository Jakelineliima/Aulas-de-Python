from rest_framework import serializers
from lavajato.models import Veiculo, Cliente, Revisao


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        field = ['id', 'modelo', 'placa', 'cor', 'fabricacao']


class RevisaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revisao
        field = ['id', 'placa', 'fabricacao', 'revisao']


class ListaRevisaoClienteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='revisao.placa')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Revisao
        fields = ['placa', 'revisao']

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaClientesRevisaoSerializer(serializers.ModelSerializer):
    cliente_id = serializers.ReadOnlyField(source='cliente.id')
    cliente_nome = serializers.ReadOnlyField(source='cliente.nome')
    cliente_cpf = serializers.ReadOnlyField(source='cliente.cpf')

    class Meta:
        model = Revisao
        fields = ['cliente_id', 'cliente_nome', 'cliente_cpf']
