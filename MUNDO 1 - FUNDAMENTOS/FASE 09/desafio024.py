# criar um programa que leia uma cidade e diga se ela começa ou não com nome "santo".

cid = str(input('Digite um nome de uma cidade: ')).lower().strip()

separa = cid.split()

print(separa[0] in 'santo')

#print(cid.find('santo')) 