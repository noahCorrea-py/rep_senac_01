# Agora, a nossa pizzaria está cobrando uma taxa fixa de R$5 por entrega, além de R$1 por km até 5km, e R$2 por km 
# até 10km. Mais ainda não entregamos com a distância superior a 10km.

# Pegando como base essas possibilidades, faça um programa que responda as seguintes perguntas:
# Quanto Joana irá pagar de frete, sendo que mora a 8km da pizzaria.
# Quanto Guilherme irá pagar de frete, sendo que mora a 3km da pizzaria.
# Quanto Rafael irá pagar de frete, sendo que mora a 11km da pizzaria.

nome = input("Qual seu nome?")
distancia = int(input("Qual a distância da entrega?"))

if distancia <= 5:
    taxa_total = 5 + distancia
    print(f'Olá, {nome}. Sua taxa de entrega vai ser de R${taxa_total:.2f} 💳')
elif distancia <= 10:
    taxa_total = 5 + (distancia*2)
    print(f'Olá, {nome}. Sua taxa de entrega vai ser de R${taxa_total:.2f} 💳')
else:
    print(f'⚠️ Olá, {nome}. Infelizmente, nossa pizzaria não entrega para distancias acima de 10km. ⚠️')
    
