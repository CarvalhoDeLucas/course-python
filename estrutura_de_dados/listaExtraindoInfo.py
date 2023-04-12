produtos = ['arroz', 'feijao', 'laranja', 'banana']

# item1, item2, item3, item4 = produtos
item1, item2, item3, *outros = produtos

print(item1)
print(item2)
print(item3)

print(outros)