# desenvlva um prgrama que leia 6 números inteiros e mostre a soma apenas daqueles que fore  PARES. Se o valor digitado for IMPAR, desconsidere.
soma = 0
cont = 0
for i in range(1,7):
    num = int(input('Digite o {} valor: '.format(i)))
    if num % 2 == 0:
        soma = soma + num
        cont += 1
if cont == 1:
    print('Você inforou {} número PAR e a soma foi: {}'.format(cont,soma))
else:
    print('Você inforou {} números PARES e a soma foi: {}.'.format(cont,soma))