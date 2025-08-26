import textwrap 

def menu():
    menu =  """\n
    ====== MENU ======
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [nc]\t Nova conta
    [lc]\t Listar contas
    [nu]\t Novo usuário
    [q]\t Sair
    =>      """

    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \t R$ {valor:.2f}\n"
        print("\n=== Depósito realizado! ===")
    else:
        print("\n!!Valor inválido!!")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    pass

def exibir_extrato(saldo, /, *, extrato):
    pass

def criar_usuario(usuarios):
    pass

def filtrar_usuario(cpf, usuarios):
    pass

def criar_conta(agencia, numero_conta, usuarios):
    pass

def listar_contas(contas):
    pass

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Valor do depósito: "))

            saldo , extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":    
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida.")

main()