valores = list()

for cont in range(0, 2):
    nome = input('Digite um nome: ')
    idade = input('Qual a sua idade? ')
    pes = float(input('Qual seu peso? '))
    alt = float(input('Qual sua altura? '))

imc = pes / alt ** 2
if imc < 18.4:
    print("Abaixo do peso")
elif imc > 18.5 and imc < 25:
    print("Peso ideal")
elif 25 <= imc <= 30:
    print("Sobrepeso")
elif imc >= 30 and imc <= 40:
    print("Obesidade")
elif imc > 40:
    print("Obesidade mórbida")

tupla = (nome,imc)
valores.append(tupla)
print('Os dados foi: {}'.format(valores))
print('o mais gordo é {}'.format(nome,imc))
