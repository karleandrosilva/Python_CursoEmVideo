# contagem de caractere em FOR:
contador = 0
texto = input('Informe seu nome: ')
for letra in texto:
    contador += 1
    print(contador, letra)
print(f'Seu nome tem {contador} letras')

# contagem de caractere em WHILE:
texto2= input('Digite seu nome: ')
c = 0
cont= 0
while c < len(texto2):
    cont += 1
    print(cont,texto2[c])
    c += 1
print(f'Seu nome tem {cont} letras')