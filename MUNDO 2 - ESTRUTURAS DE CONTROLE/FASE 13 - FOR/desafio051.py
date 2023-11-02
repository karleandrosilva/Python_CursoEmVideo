# fazer um programa que leia o primeiro termo e a razão de uma PA. No final, mostre as 10 primeiros termos dessa progressão.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + (10-1) * razao
for i in range(termo,decimo + razao,razao):
    print(i,end='-')
print('ACABOU!')