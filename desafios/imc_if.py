altura = float(input('Qual e a sua altura em cm: '))
peso = float(input('Qual e o seu peso em kg: '))

imc = peso / (altura/100)**2
print(f'Seu IMC e de {imc}')

if imc < 18.5:
    print('Magreza')
elif imc >= 18.5 and imc < 25:
    print('Normal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade grave')

