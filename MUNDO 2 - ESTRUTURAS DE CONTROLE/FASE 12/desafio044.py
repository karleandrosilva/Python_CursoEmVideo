# fazer um programa que calcule o valor a ser pago por um produto, cosiderando o seu preço normal e condição de pagamento:

print('--LOJA GKS--')

preco = float(input('Preço das Compras: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/pix
[ 2 ] à vista cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco - (preco * 10/100)
    print('Sua compra de R${:.2f}. Vai custar R${:.2f} no final.'.format(preco, total))
elif opcao == 2:
    total = preco - (preco * 5/100)
    print('Sua compra de R${:.2f}. Vai custar R${:.2f} no final.'.format(preco, total))
elif opcao == 3:
    parcela = preco / 2
    print('Sua compra será parcelada em 2x de {:.2f}'.format(parcela))
elif opcao == 4:
    parcelas = int(input('Quantas Parcelas? '))
    total = preco / parcelas 
    total_juros = preco + (preco * 20/100)
    print('A compra será parcelada em {}x de {:.2f} COM JUROS.'.format(parcelas, total))
    print('Sua compra de R${:.2f}. vai custar R${:.2f} no final.'.format(preco,total_juros))
else:
    print('COMANDO INVÁLIDO, TENTE NOOVAMENTE!')





