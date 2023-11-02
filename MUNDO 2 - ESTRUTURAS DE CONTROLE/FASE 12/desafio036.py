# escrever um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o sálario do comprador e em quantos anos ele vai pagar.

casa = float(input('Informe o valor da casa R$'))
salario = float(input('Informe o seu salário R$'))
anos = int(input('Informe quantos anos de financiamento: '))


prestacao = casa / (12 * anos)
minimo = (salario * 30/100)

print('Para pagar uma casa de {:.2f} em {} anos a prestação será de R$ {:.2f} por mês.'.format(casa, anos, prestacao))

if prestacao <= minimo:
    print('PARABÉNS! EMPRÉSTIMO ACEITO!')
    print('O valor da prestação mensal será de: {:.2f}'.format(prestacao))
else:
    print('POXA! EMPRESTIMO NEGADO!')

