<<<<<<< HEAD
galera = []
dados = []
total_max = total_min = 0
for contador in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:]) #fazer uma cópia para colocar DADOS dentro da GALERA.
    dados.clear() # excuir

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade.')
        total_max += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        total_min += 1
        
=======
galera = []
dados = []
total_max = total_min = 0
for contador in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:]) #fazer uma cópia para colocar DADOS dentro da GALERA.
    dados.clear() # excuir

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade.')
        total_max += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        total_min += 1
        
>>>>>>> 3eff50a18a354c9d60b98d6b0466bd0988a7266c
print(f'Temos {total_max} maoires e {total_min} menores de idade.')