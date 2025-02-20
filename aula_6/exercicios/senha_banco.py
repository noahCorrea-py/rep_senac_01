# Crie um sistema que peça para o usuário digitar uma senha para acessar sua conta bancária. Ele tem **apenas 3 tentativas** para acertar a senha correta. Se ele errar as 3 vezes, o sistema bloqueia a conta.

# - A senha correta é "1234".
# - O usuário tem ATÉ 3 TENTATIVAS para acertar.
# - Se errar as 3 vezes, exiba "🚫 Conta bloqueada!".

SENHA_CORRETA = 1234
tentativas = 3

while tentativas > 0:
    senha = int(input("Digite sua senha do banco:"))

    if senha == SENHA_CORRETA:
        print("🔓 Senha correta! Acesso permitido.")
        break 
    else: 
        tentativas -= 1
        print(f"Senha incorreta. Tentativas restantes: {tentativas}/3")

if tentativas == 0:
    print("🚫 Conta bloqueada! Contate sua agência para desbloquear.")
    



