# Programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado pelo usuário. O prograa será interrompido quando o número solicitado for negativo.
num = ""
while True:  
    num = int(input('Informe a tabuada que você irá querer: '))
    print('-'*40)
    if num < 0:
        break
    else:
        for c in range (1,11):
            tab = num * c
            print(f'{num} x {c} = {tab}')
print(f'Tabuada encerrada!')