# Os conjuntos são coleções não ordenadas que não permitem elementos duplicados. São úteis para gerenciar itens únicos.

# Vamos armazenar os ingredientes disponíveis sem repetições:
ingredientes = {"mussarela", "calabresa", "tomate", "azeitona"}
print("Ingredientes básicos:", ingredientes)

### OPERÇÕES COM CONJUNTOS ###

# Adicionar um novo item:
ingredientes.add("orégano")
print("Ingredientes atualizados:", ingredientes)

# Remover um item:
ingredientes.remove("azeitona")
print("Ingredientes após remoção:", ingredientes)

# União de conjuntos:
adicionais = {"bacon", "palmito"}
todos_ingredientes = ingredientes.union(adicionais)
print("Todos os ingredientes:", todos_ingredientes)

# Interseção de conjuntos:
pizza_vegana = {"tomate", "azeitona", "rúcula"}
comuns = ingredientes.intersection(pizza_vegana)
print("Ingredientes em comum:", comuns)