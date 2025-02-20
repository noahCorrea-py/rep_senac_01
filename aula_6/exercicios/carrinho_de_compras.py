# Crie um programa que permita adicionar produtos a um carrinho de compras. O programa deve continuar pedindo produtos até que o usuário digite "finalizar". No final, exiba todos os produtos comprados.

# - O usuário digita o nome do produto e ele é adicionado a uma lista.
# - Se o usuário digitar "finalizar", o programa encerra e mostra os produtos comprados.

cardapio = ["salgado", "refrigerante", "água", "café", "pão", "queijo", "presunto"]

print(f"""
==================================
           🍞 PADARIA!
==================================
PRODUTOS DISPONÍVEIS:
{cardapio}              
""")

produtos = input("🛒 Digite o produto que você deseja adicionar ao carrinho ou 'finalizar' para sair")
carrinho = []


while produtos.lower() != "finalizar": 

    if produtos.lower() in cardapio:
        carrinho.append(produtos)
        print(f"✅ {produtos} adicionado ao carrinho!")
        produtos = input("🛒 Digite o produto que você deseja adicionar ao carrinho ou 'finalizar' para sair")
    else: 
        print ("O produto não está no cardápio. Tente novamente.")
        produtos = input("Digite o produto que você deseja adicionar ao carrinho ou 'finalizar' para sair")

if len(carrinho) > 0:
    print(f"""
==================================
        COMPRA ENCERRADA
==================================
              
Seu carrinho:
""")
    for item in carrinho:
        print(f"‣ {item}")
else:
    print("Nenhum produto foi comprado. 😿")








