# SINTAXE BÁSICA DE UMA FUNÇÃO

def nome_da_funcao(parametros):
    # código da função
    resultado = 0
    return resultado

#######

# Função sem retorno
def ola_mundo():
    print ("Olá mundo! :)")

ola_mundo() # Chamando a função (invocando a função)

# Função com parâmetros
def saudacao(nome):
    print(f"Olá, seja bem vindo(a) {nome}")

saudacao("Noah")
saudacao("Nicolas")

# Função com parâmetros e retorno
def somar(num1, num2):
    soma = num1 + num2
    return soma

print(somar(5,7))
