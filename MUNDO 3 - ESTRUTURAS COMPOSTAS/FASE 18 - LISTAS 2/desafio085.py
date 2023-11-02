<<<<<<< HEAD
# programa onde o úsuario possa digitar sete valores númericos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. No final mostre os valores pares e ímares em ordem crescente. 

num = [[],[]]
valor = 0
for contador in range(1,8):
    valor = int(input(f'Digite o {contador}o. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-'*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares foram: {num[0]}')
=======
# programa onde o úsuario possa digitar sete valores númericos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. No final mostre os valores pares e ímares em ordem crescente. 

num = [[],[]]
valor = 0
for contador in range(1,8):
    valor = int(input(f'Digite o {contador}o. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-'*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares foram: {num[0]}')
>>>>>>> 3eff50a18a354c9d60b98d6b0466bd0988a7266c
print(f'Os valores ímpares foram: {num[1]}')