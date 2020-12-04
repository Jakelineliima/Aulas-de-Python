while True:
    n = int(input('Qual tabuada deseja ver? '))
    print('-'* 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'* 30)