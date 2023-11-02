# desenvolva uma lógica que leia o peso e a aultura de uma pessoa, e calcule seu IMC e mostre o status.

peso = float(input('Informe seu peso em (kg): '))
altura = float(input('Informe sua altura em (m): '))
imc = peso / (altura ** 2)
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal, cuidado!.')
elif imc >= 18.5 and imc < 25:
    print('Você está com PESO IDEAL.')
elif imc >= 25 and imc < 30:
    print('Você está com SOBREPESO.')
elif imc >= 30 and imc < 40:
    print('Você está com OBESIDADE, cuidado!')
#elif imc >= 40:
else:
    print('Você está com OBESIDADE MÓRBITA, cuidado!')