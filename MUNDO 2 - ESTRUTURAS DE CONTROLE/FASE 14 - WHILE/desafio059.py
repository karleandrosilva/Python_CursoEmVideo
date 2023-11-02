# criae um programa que leia dois valores e mostre em um menu.

jogador = 0
sair = 5
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
while jogador != sair:
    jogador = int(input('''O QUE VOCÊ QUER FAZER COM ESSES DOIS NÚMEROS:
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA
    Qual é sua opção? '''))
    if jogador == 1:
        print('A SOMA ENTRE {} + {} = {}'.format(n1, n2, n1 + n2))
        print('=-'*15)
    elif jogador == 2:
         print('A MULTIPLICAÇÃO ENTRE {} x {} = {}'.format(n1, n2, n1 * n2))
         print('=-'*15)
    elif jogador == 3:
        if n1 > n2:
            print('O NÚMERO {} É MAIOR QUE O NÚMERO {}.'.format(n1, n2))
            print('=-'*15)
        elif n2 > n1:
            print('O NÚMERO {} É MAIOR QUE O NÚMERO {}.'.format(n2, n1))
            print('=-'*15)
        else:
            print('OS DOIS NÚMEROS SÃO IGUAIS.')
            print('=-'*15)
    elif jogador == 4:
        print('=-'*15)
        n1 = int(input('Digite o primeiro valor novamente: '))
        n2 = int(input('Digite o segundo valor novamente: '))
    else:
        print('OPÇÃO INVÁLIDA')
print('PROGRAMA FECHADO!')