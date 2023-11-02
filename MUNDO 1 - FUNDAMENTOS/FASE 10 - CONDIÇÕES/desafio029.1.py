'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

# ler velocidade.
velo = int(input('Informe a velocidade atual do carro: '))

# limite
limite = 80

# se a velocidade for maior que o limite será multado.
if velo > limite:
    print('VOCÊ FOI MULTADO! Voce excedeu  limite permitido que é de 80Km/h')

    # calculando quantos km passou.
    # para saber, fiz uma subtração da velocidade com o limite.
    multa = velo - limite

    # cada km vai custar 7 reais.
    # para saber o custo, mutipliquei a multa por 7.
    custo_multa = multa * 7

    # (velo - 80) * 7

    print('Você pagará uma multa de R${:.2f} reais, pois passou de 80km, e percorreu mais {}km e cada km é 7 reais.'.format(custo_multa, multa))

# se não, não será multado.
else:
    print('Tenha um bom dia! Dirija com segurança!')
