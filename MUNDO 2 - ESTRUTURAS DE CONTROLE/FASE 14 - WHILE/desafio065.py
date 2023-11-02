# criar um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maor e o menor valores lidos. O programa deve perguntar ao usúaio se ele quer ou não CONTINUAR a digitar valores. 
resp = 's'
media = 0
quant = 0
soma = 0
maior = 0
menor = 0
# media = quant = soma = maior = menor = 0
while resp in 'sS':
    num = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N] '))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor: 
            menor = num
media = soma / quant
print('Você digitou {} números e a media foi: {:.2f}'.format(quant, media))
print('O maior número foi {}\nE o menor foi {}'.format(maior, menor))
