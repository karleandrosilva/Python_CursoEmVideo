# perguntar nome
nome = str(input('Qual é o seu nome? '))
# se o nome for gustavo, falar que é lindo. (SIMPLES)
if nome == 'gustavo':
    print('Que nome lindo você tem!')

# se o nome for esses, falar que é popular. (ANINHADA)
elif nome == 'pedro' or nome == 'karle':
    print('Seu nome é bem popular no Brasil')

# se não, falar que é normal. (COMPOSTA)
else:
    print('Que nome normal você tem!')
# dar bom dia
print('Bom dia,', nome)