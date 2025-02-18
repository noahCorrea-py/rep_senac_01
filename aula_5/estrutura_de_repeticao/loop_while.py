sabores = ["mussarela", "calabresa", "frango com catupiry", "quatro queijos", "pepperoni"]
print(f"""
============================
  🍕 Sabores disponíveis:
  {sabores}
============================
""")

pedido = ""

print("📞 Faça seu pedido (digite 'sair' para encerrar): ")
while pedido.lower() != 'sair':
    pedido = input("Escolha um sabor de pizza do cardápio: ")
    if pedido.lower() in sabores: 
        print(f'🙆‍♂️ {pedido} adicionado ao seu pedido!')
    elif pedido.lower() == 'sair':
        print("😢 Pedido encerrado!")
    else:
        print('🙅‍♂️ Esse sabor não está disponível no cardápio. Escolha outro!')