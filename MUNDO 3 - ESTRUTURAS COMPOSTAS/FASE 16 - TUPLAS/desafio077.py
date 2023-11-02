# programa que tenha uma tupla com vários 
vogais = ('a', 'e', 'i', 'o', 'u')
palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
for palavra in palavras:
    print(f'Na palavra {palavra} temos ', end='')
    for letras in palavra:
        if letras.lower() in vogais: #lower = deixar letra maiuscula para minúscula
            print(letras.lower(),end=' ')
    print()
