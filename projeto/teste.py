altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))

imc = peso / altura ** 2

print("Seu IMC é: %.4f" % imc)

if imc < 18.4:
    print("Abaixo do peso")
elif imc > 18.5 and imc < 25:
    print("Peso ideal")
elif imc >= 25 and imc <=30:
    print("Sobrepeso")
elif imc >= 30 and imc <=40:
    print("Obesidade")
elif imc >40:
    print("Obesidade mórbida")


