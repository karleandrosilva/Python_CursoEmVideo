# Programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. E no final mostrar: Qual é o total gasto da compra; Quantos produtos custam mais de R$1000; Qual é o nome do produto mais barato.

print('-'*22)
print('   LOJA ELETRO MAX   ')
print('-'*22)
contador_produto1k = preco = total_preco = 0
menor_preco = contador_preco = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    total_preco += preco
    if preco > 1000:
        contador_produto1k += 1
    if contador_preco == 1 or preco < menor_preco:
        menor_preco = preco
        barato = produto
    else:
        if preco < menor_preco:
            menor_preco = preco
            barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer Continuar? [S/N]: ').upper()
    if resposta == 'N':
        break
print('-=---FIM DO PROGRAMA-----')
print(f'O total da compra foi R${total_preco}')
print(f'Temos {contador_produto1k} produto custando mais de R$1.000,00')
print(f'O produto mais barato, foi {barato} custa R${menor_preco:.2f}')
