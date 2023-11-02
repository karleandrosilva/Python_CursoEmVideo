<<<<<<< HEAD
# tupla pode modificar
num = [1, 2, 0, 4]
print(num) # num = [1,2,0,4]
num[2] = 3 # a posição 2 deixou de ser 0 e virou 3
print(num)
num.append(6) # adiconei 5 no final.
print(num)
num.insert(4,5) # adicionei o 5 colocando na posição 4.
print(num)
num.insert(0,0) # adicionei o 0 colocando na posição 0.
print(num)
num.sort(reverse=True) # do maior para menor
print(num)
num.sort()
print(num)
num.pop(6) #remover o sexro elemento.
print(num)
print(f'Esaa lista tem: {len(num)} elementos') # tamanho da lista (qunatos elementos)
remov = int(input('Informe um número para remover: '))
if remov in num:
    num.remove(remov)
    print(num)
    print(f'Pronto! o número {remov} foi removido ')
    
else:
    print(f'Número {remov} não removido, pois não existe na lista.')
    desej = str(input(f'Deseja adicionar o {remov} na lista? S/N  '))
    if desej == 's' or 'S':
        num.append(remov)
        num.sort()
        print(num)
        print(f'Pronto! o número {remov} foi inserido na lista.')
    else:
        print(f'Ok, não irei adicionar o {remov} na lista.')
=======
# tupla pode modificar
num = [1, 2, 0, 4]
print(num) # num = [1,2,0,4]
num[2] = 3 # a posição 2 deixou de ser 0 e virou 3
print(num)
num.append(6) # adiconei 5 no final.
print(num)
num.insert(4,5) # adicionei o 5 colocando na posição 4.
print(num)
num.insert(0,0) # adicionei o 0 colocando na posição 0.
print(num)
num.sort(reverse=True) # do maior para menor
print(num)
num.sort()
print(num)
num.pop(6) #remover o sexro elemento.
print(num)
print(f'Esaa lista tem: {len(num)} elementos') # tamanho da lista (qunatos elementos)
remov = int(input('Informe um número para remover: '))
if remov in num:
    num.remove(remov)
    print(num)
    print(f'Pronto! o número {remov} foi removido ')
    
else:
    print(f'Número {remov} não removido, pois não existe na lista.')
    desej = str(input(f'Deseja adicionar o {remov} na lista? S/N  '))
    if desej == 's' or 'S':
        num.append(remov)
        num.sort()
        print(num)
        print(f'Pronto! o número {remov} foi inserido na lista.')
    else:
        print(f'Ok, não irei adicionar o {remov} na lista.')
>>>>>>> 3eff50a18a354c9d60b98d6b0466bd0988a7266c
