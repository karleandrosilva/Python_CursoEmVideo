# Leia duas notas de um aluno, e calcule a média

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda  nota: '))

#media = (n1+n2)/2
#print('A sua média é: ', media)

print('A sua média é: {:.1f}'.format((n1 + n2)/2))
