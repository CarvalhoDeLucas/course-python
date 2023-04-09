valor = int(input('Digite o valor do seu produto em RS: '))

while valor > 20:
    valor += (valor * 0.10)
    print(f'O valor final do seu produto sera de RS{valor}')
    break