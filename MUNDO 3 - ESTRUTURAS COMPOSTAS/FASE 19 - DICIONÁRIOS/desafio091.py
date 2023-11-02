# programa onde 4 jogadores joga um dado e tem resultados aleatórios. Ele irá guardar esses resultados em um dicionário. E no final, o dionário é colocado em ordem, mostrando que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1' : randint(1,6),
    'Jogador 2' : randint(1,6),
    'Jogador 3' : randint(1,6),
    'Jogador 4' : randint(1,6)}

ranking = {}

print('Valores sorteados:')
for keys, valor in jogo.items():
    print(f'{keys} tirou {valor} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('==RANKING DOS JOGADOORES==')
for indice, valorr in enumerate(ranking):
    print(f'{indice+1}º lugar: {valorr[0]} com {valorr[1]}.')
    sleep(1)
