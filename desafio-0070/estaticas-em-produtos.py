print('Loja de departamento !')
total = totmil = less = cont = 0
lowprice = ' '
while True:
    product= str(input('Nome do produto: '))
    price = float(input('Preço do produto: ')) 
    cont += 1
    total += price
    if price >= 1000:
       totmil += 1
    if cont == 1 or price < less:    
        less = price
        lowprice = product
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':    
            break    
print(f'Total da compra foi: {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {lowprice} que custa R${less:.2f}')