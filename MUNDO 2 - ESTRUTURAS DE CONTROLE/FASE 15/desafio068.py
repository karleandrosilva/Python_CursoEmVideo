# Programa que joga par ou impar com o usuário. O jogo só será interrompido quando o jogador PERDER mostrando o total de vitórias consecutivos que ele conquistou no final do jogo.
from random import randint
vitoria = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('[P]AR ou [I]MPAR ? ')).upper()
    print(f'Você jogou {jogador} e o Computador {computador}. Total de {total}')
    print('DEU PAR!' if total % 2 == 0 else 'DEU IMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')

print(f'GAME OVER! Você venceu {vitoria} vez.'if vitoria <= 1 else'GAME OVER! Você venceu {vitoria} vezes.')