pessoas = {'NOME':'Gustavo','SEXO':'M','IDADE':23}

for k in pessoas.keys():
    print(k)
print('-'*10)
for v in pessoas.values():
    print(v)
print('-'*10)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-'*10)
pessoas['NOME']= 'Karle'
pessoas['IDADE']= 19
pessoas['PESO']= '54kg'
for k, v in pessoas.items():
    print(f'{k} = {v}')