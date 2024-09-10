menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe seu valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito : R$ {valor:.2f}\n"

        else:
            print("Operação inválida! Selecione um valor válido.")


    elif opcao == "2":
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = valor >= LIMITES_SAQUES


        if excedeu_saldo:
            print("Operação FALHOU! Saldo insuficiente.")

        elif excedeu_limite:
            print("Operação inválida! O valor solicitado excede o limite de saque.")

        elif excedeu_saque:
            print("Operação inválida! Número máximo de saques realizado.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"

        else:
            print("Operação inválida! O valor não é valido.")

    elif opcao == "3":
        print("\n ********** EXTRATO **********")
        print("Não foram realizadas operações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n *****************************")

    elif opcao =="4":
        break

    else:
        print("Operação inválida! Informe a opção desejada.")