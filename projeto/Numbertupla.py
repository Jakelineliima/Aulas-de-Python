numero = []
par = []
print('Coloque numeros entre 1 a 10')
for n in range(1, 6):
    a = int(input('Digite um número:  '))
    numero.append(a)
print(f'A quantidade de nove é: {numero.count(9)}')
for b in numero:
    if b % 2 == 0:
        par.append(b)
    if b == 3:
        print(f' A posição do três é: {numero.index(3)+1} ')
print(f'Numeros pares são {par}')