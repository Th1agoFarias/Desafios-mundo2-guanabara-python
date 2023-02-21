print('--- Cadastre uma pessoa ---')
menoridade=  quanthomens = totmulher20 = 0
while True:
    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
         sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if idade >=18:
        menoridade +=1
    if sexo in 'Mm':
        quanthomens += 1
    if sexo in 'F' and idade < 20:
        totmulher20  += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':    
            break    
print(f'Ao todos são {quanthomens} homens')
print(f'Ao todo são {menoridade} com menos de 18 anos !')
print(f'Ao todo são {totmulher20} mulher com menos de 20 anos')                        


