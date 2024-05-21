# programa que gerencia o aproveitamento de um jogador de futebol. o programa vai ler o nome do jogador e quatas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
partidas = []
soma = 0

jogador['NOME'] = str(input('Nome do Jogador: '))
total = int(input(f'Quantas partidas {jogador["NOME"]} jogou: '))
for cont in range(0, total):
    partidas.append(int(input(f'Quantos gols na partida {cont+1}: '))) 
jogador['GOLS'] = partidas[:]

# SOMA DOS GOLS
for partida in partidas:
    soma += partida
jogador['TOTAL'] = soma
# jogador['TOTAL'] = sum(partidas)

print(jogador)
print('+='*20)
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}.')
print('+='*20)

print(f'O jogador {jogador["NOME"]} jogou {len(jogador["GOLS"])} partidas.')
for i, v in enumerate(jogador['GOLS']):
    print(f'    => Na Partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["TOTAL"]} gols.')