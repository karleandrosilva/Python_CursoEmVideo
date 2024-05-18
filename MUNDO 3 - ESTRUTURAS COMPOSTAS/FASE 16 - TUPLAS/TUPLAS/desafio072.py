# Programa que tem uma tupla totalmente preechida com uma contagem por extenso de zero até vinte. Deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis','sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n >= 0 and n <= 20:
        break
    print(f'Tente novamente.',end=' ')
print(f'Você digitou o número {numeros[n]}.')
#continuar = input('Quer continuar? S/N: ')
print('FIM!')