# As tuplas são coleções ordenadas, porém imutáveis. Use-as quando você não precisar alterar os dados após criá-los.

# Vamos definir os tamanhos de pizzas disponíveis (essas informações não mudam):
tamanhos = ("pequena", "média", "grande")
print("Tamanhos disponíveis:", tamanhos)

### OPERÇÕES COM TUPLAS ###

# Acessar itens:
print("Tamanho médio:", tamanhos[1])

# Verificar itens:
print("Existe tamanho grande?", "grande" in tamanhos)