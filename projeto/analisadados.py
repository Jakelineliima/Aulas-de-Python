somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ''
mulher = 0
for p in range(1, 5):
    print('-----{}ª Pessoa -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1

mediaidade = somaidade / 4
print(' A média da idade é {} anos'.format(mediaidade))
print('O homen mais velho tem {} anos e se chama {}'.format(maioridade, nomevelho))
print('Total de mulheres com menos de 20 anos são: {} '.format(mulher))