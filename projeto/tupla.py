from random import randint
n = (randint(1, 100),randint(1, 100),randint(1, 100),randint(1, 100),randint(1, 100),randint(1, 100),randint(1, 100),
     randint(1, 100),randint(1, 100),randint(1, 100))
print(f'Os valores sorteado foi: {n} ')

print(f'O menor valor sorteado foi: {min(n)}')
print(f'O maior valor sorteado foi: {max(n)}')
print(sorted(n))