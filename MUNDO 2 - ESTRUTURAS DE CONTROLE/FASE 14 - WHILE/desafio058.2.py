from random import randint
pc = randint(0, 5)
print('Acabei pensando em um número entre 0 e 10')
print('Será que você consegue adivinhar!')
acertou = False
cont_palpite = 0
while not acertou:
    jo = int(input('Informe o número: '))
    cont_palpite = cont_palpite + 1
    if jo == pc:
        acertou = True
        print('PARABÉNS! VOCÊ VENCEU!')
    else:
        if jo < pc:
            print('Mais... Tente novamente!')
        elif jo > pc:
            print('Menos... Tente novamente!')
print('Foram necessários {} vezes para vencer!'.format(cont_palpite))
