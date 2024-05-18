# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoa = {}
pessoas = []
continuar = 'S'
soma = media = 0

while continuar == 'S':
    pessoa.clear() # apago o que tinha antes
    pessoa['nome'] = str(input('Informe seu nome: '))

    while True:
        pessoa['sexo'] = str(input('Informe seu sexo: [M/F]: ')).upper()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F: ')

    pessoa['idade'] = int(input('Digite sua idade: '))
    soma += pessoa['idade']

    pessoas.append(pessoa.copy()) #adiciono na lista e duplico

    while True:
        continuar = str(input('Deseja continuar? Digite [S/N]: ')).upper()
        if continuar in 'SN':
            break
        print('ERRO! Por favor, responda S ou N: ')

media = soma / len(pessoas)
print(pessoas)
print('-'*30)
print(f'A) QUANTIDADE DE CADASTRADOS: {len(pessoas)}') #len é para ver o tamanho da lista
print(f'B) MÉDIA DE IDADES É: {media:.2f} ANOS')
print(f'C) MULHERES CADASTRADAS: ', end='')
for mulher in pessoas:
    if mulher['sexo'] == 'F':
        print(f'{mulher["nome"]} ')

print('D) PESSOAS COM IDADE ACIMA DA MÉDIA: ', end='')
for idade in pessoas:
    if idade['idade'] >= media:
        print('    ', end='')
        for k, v in idade.items():
            print(f'{k} = {v}; ', end='')
        print()
print('  << ENCERRADO >> ')