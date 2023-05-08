def quantidade_latas(rendimento, altura, largura):
    total_latas = (altura * largura) / rendimento
    return total_latas

rendimento = int(input('Qual o rendimento da tinta? '))
altura = int(input('Qual a altura da parede? '))
largura = int(input('Qual a largura da parede? '))

total = quantidade_latas(rendimento, altura, largura)

print('Vc precida de ' + str(total) + ' latas de tinta')
