print('*** Confederação Nacinal de natação ***')

nome = str(input('Seu nome: '))
idade = int(input('Sua idade, por favor: '))

if idade < 9:
    print(f'{nome} sua categoria conforme a sua idade de {idade} é MIRIM ')
elif idade < 14:
    print(f'{nome} sua categoria conforme a sua idade de {idade} é IFANTIL ')
elif idade < 19:
    print(f'{nome} sua categoria conforme a sua idade de {idade} é JÚNIOR ')
elif idade < 20:
    print(f'{nome} sua categoria conforme a sua idade de {idade} é SÊNIOR ')    
else :
    idade >= 20
    print(f'{nome} sua categoria conforme a sua idade de {idade} é MASTER') 