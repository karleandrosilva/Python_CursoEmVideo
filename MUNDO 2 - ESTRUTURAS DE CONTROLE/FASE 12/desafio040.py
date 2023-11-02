#  crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atinginda.


print('----------------')
print('-MÉDIA DO ALUNO-')
print('----------------')

nota1 = float(input('Digite sua primeira nota: '))

nota2 = float(input('Digite sua segundaa nota: '))

media = (nota1 + nota2) / 2

print('A sua média foi: {:.1f}'.format(media))

if media < 5.0:
    print('Você está REPROVADO!')
elif media >=5 and media <7:
    print('Você está de RECUPERAÇÃO!')
else:
    print('Você está APROVADO!')