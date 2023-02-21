n=s=quant=0
while True:
    n=int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    quant += 1
print(f'A soma vale: {s}')    
print(f'Você digitou: {quant}')    