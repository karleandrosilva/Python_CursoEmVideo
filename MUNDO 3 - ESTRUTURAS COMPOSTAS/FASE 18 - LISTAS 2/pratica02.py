teste = []
teste.append('Gustavo')
teste.append(40)
#print(teste) ['Gustavo', 40]
galera = []
galera.append(teste[:]) # fazer uma cópia: []
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) # galera.append(teste)
print(galera) # [['Gustavo', 40]]
