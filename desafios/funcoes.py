rendimento = int(input('Qual o rendimento da tinta? '))
altura = int(input('Qual a altura da parede? '))
largura = int(input('Qual a largura da parede? '))

def quantidade_latas():
    total_latas = (altura * largura) / rendimento
    print(f'Vc precida de {str(total_latas)} latas de tinta')

quantidade_latas()