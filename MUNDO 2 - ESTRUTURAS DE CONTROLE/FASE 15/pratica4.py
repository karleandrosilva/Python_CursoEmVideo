n = s =  0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break #vai parar quando o num é 999
    s += n
print(f'A soma vale {s}')