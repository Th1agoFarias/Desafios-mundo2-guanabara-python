primeiro= int(input('Primeiro elemento: '))
r = int(input('Razão: '))
n = int(input('Quantos elementos exibir: '))

ultimo = primeiro + (n-1)*r
ultimo = ultimo + 1

for v in range(primeiro, ultimo, r):
    print(v)