from random import randint
pc = randint(0, 5)
jo = 0
cont_palpite = 0
print('Acabei pensando em um número entre 0 e 10')
print('Será que você consegue adivinhar!')
while jo != pc:
    jo = int(input('Informe o número: '))
    cont_palpite = cont_palpite + 1
    if jo == pc:
        print('PARABÉNS! VOCÊ VENCEU!')
    elif jo > pc:
        print('Mais... Tente novamente!')
print('Foram necessários {} vezes para vencer!'.format(cont_palpite))
