a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # junta A mais B
d = b + a # junta B mais A
print(c)
print('-'*20)
print(d)
print('-'*20)
print(f'O número 5 aparece {c.count(5)} vezes') # count = quantas vezes aparece algo
print('-'*20)
print(f'O número 8 está na posição: {d.index(8)}') # index = mostra qual posição está