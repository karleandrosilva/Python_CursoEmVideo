viagem = float(input('Digite a distância da viagem: '))
if viagem <= 200:
    preco1 = viagem *  0.50
    print('O preço da passagem é:', preco1,'reais')
else:
    preco2 = viagem *  0.45
print('O preço da passagem é:', preco2,'reais')

