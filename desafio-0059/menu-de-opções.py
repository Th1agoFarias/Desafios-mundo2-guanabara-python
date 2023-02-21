print('*** Menu de opções ***')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

while True:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    ''')

    escolha = int(input('Digite uma opção: '))

    if escolha == 1 :
        s = n1 + n2
        print(f'A soma entre {n1} e {n2} é igual {s}')
    
    elif escolha ==2:
        m = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é igual  {m}') 
   
    elif escolha ==3:
       if n2 > n1:
        print(f'O maior número entre {n1} e {n2} é o {n2}')
    elif n1 < n2:
        print(f'O maior número entre {n1} e {n2} é o {n1}')
    elif n2 == n1:
        print(f'Os números digitados são iguais !')   
    
    elif escolha == 4:
        n1 = int(input('Digite o primeiro número novamente: '))
        n2 = int(input('Digite o segundo número novamente: '))
    
    elif escolha == 5:
        print('Programa encerrado !')
        break
    else:
        print('Escolha inválida !')    
         
