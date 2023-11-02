estado = {}
brasil = []

for contador in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['SIGLA'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)

# for estado in brasil:
#     print(estado)

for estado in brasil:
    for valor in estado.values():
        print(valor, end=' ')
    print()
