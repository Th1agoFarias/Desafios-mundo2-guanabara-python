n = 1
s = 0
quantidade = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 0:
        break
    s = s + n
    quantidade = quantidade + 1
print(f'Qauntidade de numéro digitados foram: {quantidade}')
print(f'A soma dos números digitados foram: {s} ')
print('Fim')    
