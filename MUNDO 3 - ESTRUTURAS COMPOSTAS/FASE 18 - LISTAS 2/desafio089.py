<<<<<<< HEAD
# programa que leia nome e duas nots de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usúario possa mostrar as notas de cada aluno individualmente.

ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]  '))
    if resp in 'Nn':
        break
print('-'*25)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*22)
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-'*25)
    opcao = int(input('Mostrar notas de qual aluno? (999 Interrompe)  '))
    if opcao == 999:
        print('FINALIZANDO!')
        break
    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
=======
# programa que leia nome e duas nots de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usúario possa mostrar as notas de cada aluno individualmente.

ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]  '))
    if resp in 'Nn':
        break
print('-'*25)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*22)
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-'*25)
    opcao = int(input('Mostrar notas de qual aluno? (999 Interrompe)  '))
    if opcao == 999:
        print('FINALIZANDO!')
        break
    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
>>>>>>> 3eff50a18a354c9d60b98d6b0466bd0988a7266c
print('<<< VOLTE SEMPRE! >>>')