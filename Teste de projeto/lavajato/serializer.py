from lavajato.models import Cliente, Veiculo

def ClienteSerializer():
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'rg', 'cpf']


def VeiculoSerializer():
    class Meta:
        model = Veiculo
        field = ['__all__']