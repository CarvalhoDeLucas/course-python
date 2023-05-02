try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Digite um valor numerico!')
else:
    print('Usuario digitou um valor correto')
    resultado = valor * 2
    print(resultado)
finally:
    print('Sempre sera executado')

print('Mais codigo abaixo')