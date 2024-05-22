#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['NOME'] = str(input('Nome do Jogador: '))
    total = int(input(f'Quantas partidas {jogador["NOME"]} jogou: '))
    partidas.clear()

    for cont in range(0, total):
        partidas.append(int(input(f'Quantos gols na partida {cont+1}: '))) 
    jogador['GOLS'] = partidas[:]
    jogador['TOTAL'] = sum(partidas)
    jogadores.append(jogador.copy())

    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).upper()
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N: ')
    if continuar == 'N':
        break

print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-'*40)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' >> LEVANTAMENTO DO JOGADOR {jogadores[busca] ["NOME"]}: ')

        for i, gols in enumerate(jogadores[busca]["GOLS"]):
            print(f'  No jogo {i} fez {gols} gols.')
    print('-'*40)
print('VOLTE SEMPRE!')