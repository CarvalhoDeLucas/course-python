# Dicionarios
    # Utiliza index no formato de Keys e Values
    # Aceita string, integer, float, boolean...

aluno = { 'nome': 'Lucas', 'idade': 22, 'nota_final': 'A', 'aprovacao': True }
print(aluno)
print(aluno['nome'])
print(aluno.get('nome'))
print(aluno.get('teste', 'Nao existe'))

aluno.update({ 'nome': 'Eduardo', 'nota_final': 'B' })
print(aluno)

aluno.update({ 'endereco': 'Rua A' })
print(aluno)

del aluno['idade']
print(aluno)