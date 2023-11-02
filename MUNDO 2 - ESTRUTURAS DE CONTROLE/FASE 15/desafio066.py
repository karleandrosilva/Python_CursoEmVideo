# Programa que lê vários números inteiros pelo teclado. E que só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostrará quantos números foram digitados e qual foi a soma entre elas deconsiderando o FLAG.
soma = cont = 0
while True:
    n = int(input(f'Digite um valor (999 para parar): '))
    if n == 999:
        break 
    soma = soma + n # soma += n SOMADOR
    cont += 1 # cont = cont + 1 CONTADOR
print(f'A soma dos {cont} valores foi {soma}!')