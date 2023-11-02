# programa que tem uma tupla com os 20 times colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. E que exiba os 5 primeiros colocados e os últimos 4, times em ordem alfabética e em que posição o 'Cuiabá' está.

times = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Fluminense', 'Bragantino', 'Athletico-PR', 'Fortaleza', 'Atlético-MG', 'Cuiabá', 'São Paulo', 'Cruzeiro', 'Corinthians', 'Internacional', 'Goiás', 'Bahia', 'Santos', 'Vasco', 'Coritiba', 'América-MG')

print(f'Os 5 primeiros colocados: ') #print(f'Os 5 primeiros colocados: {times[0:5]}')
for cont in range(0, 5):
    print(times[cont])

print('Os últimos 4 colocados:')
for c in range(-4, 0):
    print(times[c])

print(f'Lista dos times em ordem alfabética: {sorted(times)} ')

print(f'Cuiába está na: {times.index("Cuiabá")+1}º posição.')

