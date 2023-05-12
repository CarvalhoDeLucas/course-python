funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno']
turno_noite = ['Ana', 'Alice']
turno_dia = ['Marco', 'Pedro']
tem_carro = ['Marcos', 'Alice']

lista1 = set(tem_carro).intersection(turno_noite)
lista2 = set(tem_carro).intersection(turno_dia)
lista3 = set(funcionarios).difference(tem_carro)

print(lista1)
print(lista2)
print(lista3)