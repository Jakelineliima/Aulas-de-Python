preco = float(input("Preço do produto: R$ "))
print('Escolha a opção de pagamento:\n'
      '1 À vista dinheiro/cheque: 10% de desconto.\n'
      '2 À vista no cartão: 5% de desconto.\n'
      '3 Em até 2x no cartão: preço normal.\n'
      '4 3x até 12x no cartão: 20% de juros.\n'
      '5 Mais de 12 parcelas:')

v = preco - (preco * 10 / 100)
c = preco - (preco * 5 / 100)
cartao = preco - (preco * 2)
parcelado = preco + (preco * 20 / 100)

op = int(input())
if op == 1:
    v = preco - (preco * 10 / 100)
    print("Á Vista no dinheiro/cheque: R${:.2f}".format(v))
elif op == 2:
    c = preco - (preco * 5 / 100)
    print("A vista no cartão: R${:.2f}".format(c))
elif op == 3:
    print("O valor total: R${:.2f} ".format(preco))
elif op == 4:
    parcelado = preco + (preco * 20 / 100)
    print(" Em ate 12x no cartão:R${:.2f}".format(parcelado))
elif op == 5:
    print("Não é possivel no momento")
elif op > 5:
    print("Não existi mais opções de pagamento")