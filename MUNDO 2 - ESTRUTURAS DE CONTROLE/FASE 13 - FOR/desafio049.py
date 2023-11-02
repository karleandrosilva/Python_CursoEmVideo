# refazer a tabuada que o usuário escolher, com a função for. 

num = int(input('Digite um número que você quer a tabuada: '))
print('A TABUADA DO {}'.format(num))
for c in range(1,11):
    print('{} x {} = {}'.format(num, c, num * c))