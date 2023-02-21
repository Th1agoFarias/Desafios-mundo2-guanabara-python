'''
Crie um programa que leia ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas são já são maiores.
'''
from datetime import date
current_date = date.today()

for p in range(0,7):
    data = int(input('Seu ano de nascimento: '))
    idade = date.today().year-data
if idade < 18:
    print('Nenhuma pessoa atingiu a maioridade')    
else:
    print(f'O grupo que atingiu a maioridade foram {idade}')
  