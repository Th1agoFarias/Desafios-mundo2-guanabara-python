from random import randint
point =0
while True:
    player = int(input('Diga um valor: '))
    pc = randint(0, 10)
    total = player + pc
    type = ' '
    while type not in 'PI':
        type = str(input('Par ou Ímpar ? [P/I]')).strip().upper()[0]
    print(f'Você jogou {player} e o computador {pc}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if type == 'P':
        if total % 2== 0:
            print('Você VENCEU !')
            point += 1
        else:
            print('Você PERDEU !')
            break
    elif type == 'I':
        if total % 2 == 0:
            print('Você VENCEU !')
            point += 1
        else:
            print('Você Perdeu !')
            break
    print(f'Vamos jogar novamente...')
print(f'GAMER OVER ! Você venceu {point} vezes.')        



