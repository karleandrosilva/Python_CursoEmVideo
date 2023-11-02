# leia uma frase qalquer  

frase = str(input('Digite uma frase qualquer: ')).strip().upper()

print('A letra "A" aparece {} vezes'.format(frase.count('A')))

print('A primeira letra "A" apareceu na posição {}'.format(frase.find('A')+1))

print('A última letra "A" apareceu a posição {}'.format(frase.rfind('A')+1))

