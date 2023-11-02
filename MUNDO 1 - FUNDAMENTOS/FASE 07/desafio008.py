# Leia um valor em metros e o exiba convertido em CENTÍMETROS e MILÍMETROS.

m = float(input('Digite um valor em metros: '))

print('O valor {} metros, convertido para centímetros é {:.0f}cm. Já em milímetros é {:.0f}mm.'.format(m,(m*100), (m*1000)))

#cent = m * 100 
#mili = m * 1000
#print('O valor',m,'metros, convertido para centímetros é',cent,'cm. Já em milímetros é',mili,'mm.')

