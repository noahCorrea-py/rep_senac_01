# Os dicionários armazenam dados em pares chave:valor. Eles são ideais para representar informações mais estruturadas.

# Criando um cardápio com os preços de pizza:
cardapio = {
    "mussarela": 25.90,
    "calabresa": 27.90,
    "frango com catupiry": 29.90
}
print("Cardápio da Pizzaria Sabores:", cardapio)

### OPERÇÕES COM DICIONÁRIOS ###

# Acessar um valor:
print("Preço da calabresa:", cardapio["calabresa"])

# Adicionar um novo item:
cardapio["portuguesa"] = 30.90
print("Cardápio atualizado:", cardapio)

# Alterar um valor:
cardapio["mussarela"] = 26.90
print("Preço atualizado da mussarela:", cardapio["mussarela"])

# Iterar sobre os itens:
for sabor, preco in cardapio.items():
    print(f"A pizza de {sabor} custa R$ {preco:.2f}.")
