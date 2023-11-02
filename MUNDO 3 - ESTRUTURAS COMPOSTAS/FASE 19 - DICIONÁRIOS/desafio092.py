# programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade), em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contrataao e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime # para saber qual ano estamos.
dados = {}
dados['NOME'] = str(input('Nome: '))
ano_nasc = int(input('Ano de Nascimento: '))
dados['IDADE'] = datetime.now().year - ano_nasc 
dados['CARTEIRA DE TRABALHO'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CARTEIRA DE TRABALHO'] != 0:
    dados['ANO DE CONTRATAÇÃO'] = int(input('Ano de Contratação: '))
    dados['SALÁRIO'] = float(input('Salário: R$'))
    dados['APOSENTADORIA'] = (dados['IDADE'] + (dados['ANO DE CONTRATAÇÃO'] + 35) - datetime.now().year)
print('-='*15)
print(dados)
for valor, chave in dados.items():
    print(f'{valor} tem o valor {chave}')