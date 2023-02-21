print('*** Analisando Triângulos ***')
r1 = float(input('Primeiro lado: '))
r2 = float(input('Segundo lado: '))
r3 = float(input('Terceiro lado: '))

if (r1+ r2+ r3) or (r1+ r3 + r2) or (r2+ r3 + r1):
    print('Não é um triângulo ! :( ')
elif(r1 == r2) and (r1 == r3):
    print('É um triângulo Equilatero ')
elif (r1 == r2) or (r1 == r3) or (r2 == r3):
    print('É um triângulo Isósceles ')
else:
    print('É um triângulo Escaleno ')    
