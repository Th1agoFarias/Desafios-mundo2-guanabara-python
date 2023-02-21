from random import randint
from time import sleep


pergunta =('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)



print(''' Escolha uma opção para jogar !
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

user = int(input('Qual é a sua jogada ? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(2)
print('-' * 11)

print(f'Computador jogou: {pergunta[pc]}')
print(f'Jogador jogou: {pergunta[user]}')

if pc == 0:
    if user == 0:
        print('EMPATE')
    elif user ==1:
        print('VOCÊ VENCEU !')
    elif user ==2:
        print('COMPUTADOR VENCEU !') 
    else:
        print('JOGADA INVÁLIDA!')
   
if pc == 1:
    if user == 0:     
        print('COMPUTADOR VENCEU')
    elif user == 1:
        print('EMPATE') 
    elif user == 2:
        print('VOCÊ VENCEU')
    else:
        print('JOGADA INVÁLIDA!')    

if pc == 2:
    if user == 0:
        print('VOCÊ VENCEU !')
    elif user == 1:
         print('COMPUTADOR VENCEU')
    elif user == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')             