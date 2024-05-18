# programa onde o usúario digita vários valores e cadastre-os em uma lista. Caso o número já exista lá dentro ele não será adicionado. No final serão exibidos todos os valores em ordem crescente.

numeros  = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucessso...')
    else:
        print('Valor duplicado! Não vou adicionar.')
    resposta = (input('Quer continuar? [S/N]  '))
    if resposta == 'S':
        continue
    elif resposta != 's':
        break
print('-' * 30)
numeros.sort()
print('Você digitou os valores: {}'.format(numeros))