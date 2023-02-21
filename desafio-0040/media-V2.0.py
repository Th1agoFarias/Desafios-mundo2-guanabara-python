print('*** Média ***')

nome = str(input('Qual é o seu nome ? '))
print(f'Seja bem vindo, {nome}')
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))

media = (n1 + n2) / 2

if media<5.0:
    print(f'{nome}, sua média foi {media} e a sua situação é: Reprovado')
elif media < 5.0 or media <6.9:
    print(f'{nome}, sua média foi {media} e a sua situação é: Recuperação')         
else:
    media < 7.0
    print(f'{nome}, média foi {media} e a sua situação é: APROVADO com SUCESSO !')        

    
