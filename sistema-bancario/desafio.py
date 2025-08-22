menu = """

[d] depositar
[s] sacar
[e] extrato
[q] sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Valor do depósito"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("ERRO! Valor inválido")

    elif opcao == "s":
        valor = float(input("Valor do saque"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("ERRO! Saldo inválido")
        
        elif excedeu_limite:
            print("ERRO! O valor excedeu o limite ")
        
        elif excedeu_saques:
            print("ERRO! Número máximo de saques atingido")

        elif valor > 0:
            saldo -= valor
            numero_saques +=1
            extrato += f"Saque: R$ {valor:.2f}"
        
        else:
            print("ERRO! Valor inválido")

    elif opcao == "e":
        print("\n=== EXTRATO ===")
        print("Nenhuma movimentação" if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("================")
    
    elif opcao == "q":
        break

    else:
        print("Opção inválida")
    