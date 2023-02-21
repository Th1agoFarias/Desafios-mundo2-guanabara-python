'''
Faça um programa que leia um número inteiro e diga se ele é 
ou não um número primo.
'''

n = int(input('Digite um número inteiro: '))
mult = 0

for c in range(2,n):
    if (n% c == 0):
        print(f'Múltiplo de {c}' )
        mult +=1

if (mult == 0):
    print('É primo !')
else:
    print(f'Tem {mult} multiplos acima de 2 e abaixo de {n}')    
