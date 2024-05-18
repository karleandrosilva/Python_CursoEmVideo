# progama que o úsuario possa digitar cinco  valores númericos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenado na tela. 
lista = []
for c in range(0, 5):
    n = int(input(f'Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                print(f'Adicionado na posição {posicao} da lista')
                break
            posicao += 1
print('-='*30)
print(f'Os valores adicionados em ordem foram: {lista}')