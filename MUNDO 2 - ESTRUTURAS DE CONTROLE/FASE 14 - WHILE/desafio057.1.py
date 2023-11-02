sexo = str(input('Informe seu sexo: [M/F] '))
while sexo == 'MmFf' :
    sexo = str(input('Dados inválidos. Por favor, informe aeu sexo: '))
print('Sexo {} registrado com sucesso'.format(sexo))