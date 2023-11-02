# programa que lê quatro valores, digitados pelo o usúario e guarda em uma tupla. No final irá mostar, quantas vezes o número 9 apareceu, qual posição foi digitado o número 3 e quais foram os números pares.
tupla_nomes = (int(input('Digite um número: ')),
               int(input('Digite outro número: ')),
               int(input('Digite mais um número: ')),
               int(input('Digite o último número: '))
               )
print(f'Você digitou os seguintes números: {tupla_nomes}')
if 9 in tupla_nomes:
    print(f'O valor 9 apareceu {tupla_nomes.count(9)} vezes.')
if 3 in tupla_nomes:
    print(f'O valor 3 foi digitado na {tupla_nomes.index(3)+1}ª posição.')
print(f'Os números pares foram: ', end='')
for n in tupla_nomes:
    if n % 2 == 0:
        print(n, end=' ')