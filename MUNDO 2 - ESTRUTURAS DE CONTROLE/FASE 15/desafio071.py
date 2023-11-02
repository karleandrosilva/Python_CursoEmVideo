# Programa que simula o funcionamento de um caixa eletrônico. No início ele pergunte ao usúario qual será o valor a ser sacado(número inteiro) e o programa informa quantas cédulas de cada valor serão entregues. Considerando que o caixa possui cédulas de R$50, 20, 10 e 1 real
print('-'*23)
print('      BANCO KARLE     ')
print('-'*23)
valor = int(input('Que valor você quer sacar? R$'))
total_atual = valor #montante
ced = 50
total_ced = 0
while True:
    if total_atual >= ced:
        total_atual -= ced 
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total_atual == 0:
            break
print('-'*23)
print('Volte sempre ao BANCO KARLE!')