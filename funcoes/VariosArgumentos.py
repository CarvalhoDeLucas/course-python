# Criar uma funcao que soma varios numeros
def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num    
    return resultado


x = soma(1, 2, 3, 4)
print(x)

# Criar uma funcao que armazena numeros e string (dados)
def agencia(**carro):
    return carro


print(agencia(marca='Gol', cor='Branca', motor=1.0, placa=1234))