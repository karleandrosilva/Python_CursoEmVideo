# programa que lê nome e média de um aluno, guardando também a situação em um dicionário. No final mostre o conteúdo da estrutura na tela. 

aluno = {}

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5<= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('-'*15)
for key, valor in aluno.items():
    print(f'{key} é igual a {valor}')