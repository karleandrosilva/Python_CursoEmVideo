# Programa que lê a idade e o sexo de várias pessoas. A cada pessoa cadastrada, deve perguntar se o usúario quer ou não  continuar. No final mostrar: Quantas pessoas tem mais de 18 anos; Quantos homens foram cadastrados; Quantas mulheres tem menos de 20 anos. 
contador_idade = contador_homem = contador_mulher20 = 0
print('----CAD ÚNICO----')
while True:
    idade = int(input('Informe sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Informe seu sexo M/F: ').upper()
    if idade >= 18:
        contador_idade += 1
    if sexo == 'M':
        contador_homem += 1
    if sexo == 'F' and idade < 20:
        contador_mulher20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? S/N: ').upper()
    print('CADASTRADO COM SUCESSO!')
    print('-----------------------')
    if resposta == 'N':
        break
print(f'TOTAL DE MAIORES DE IDADE: {contador_idade}')
print(f'TOTAL DE HOMENS CADASTRADO: {contador_homem}')
print(f'TOTAL DE  MULHERES COM MENOS DE 20 ANOS: {contador_mulher20}')