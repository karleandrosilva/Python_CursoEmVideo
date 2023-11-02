# saber a velocidade
velocidade = int(input('Qual é a velocidade que você está indo? '))

# limite de 80km
limite = 80

# se a velocidade for maior que 80km
if velocidade > limite:

    # sera multado
    print('VOCÊ FOI MULTADO!') 

    # saber quantos km
    multa1 =  velocidade - limite

    # calcular cada km vezes 7 reais
    multa2 = multa1 * 7

    # valor da multa
    print('VOCÊ PAGARÁ:', multa2,'reais de multa!')

# se não, não sera multado
else:
    print('VOCÊ NÃO FOI MULTADO!')
    