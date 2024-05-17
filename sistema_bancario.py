import textwrap

def menu():
    menu = """ \n
    ==============MENU==============

    [1]\t DEPÓSITO
    [2]\t SAQUE
    [3]\t EXTRATO
    [4]\t CONTA NOVA
    [5]\t LISTA DE CONTAS
    [6]\t NOVO USUÁRIO
    [7]\t SAIR

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo +=valor
        extrato+= f"Depósito:\tR$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso!!!")
    else:
        print("\n O valor informado é inválido. Tente novamente!!!!")    

    return saldo, extrato    

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor >limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n Você não tem saldo suficiente!!")

    elif excedeu_limite:
        print("\n O valor de saque excede o limite!!!")

    elif excedeu_saques:
        print("\n Número máximo de Saques excedido!!!!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"    
        numero_saques += 1
        print("\n Saque Realizado com Sucesso!!!")

    else:
        print("\n O valor informado é inválido!!!")    

    return saldo, extrato 

def exibir_extrato(saldo, /, *, extrato):
    print("\n ======================EXTRATO=================")
    print("Não foram realizados movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==================================================")

def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF: ")
    usuario = filtar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF!!")
        return
    
    nome = input("informe o Nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço completo(logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso!!!")

def filtar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]== cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o CPF do usuário: ")
    usuario = filtar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!!")
        return { "agencia":agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n Usuário não encontrado, processo encerrado!!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
    """    
    # print("=" * 100)    
    # print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("informe o valor de depósito: "))
            print(f"Valor de R$ {valor:.2f} foi depositado com sucesso!")

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":        
            valor  = float (input("informe o valor do saque: "))
            print(f"Saque de R${valor:.2f} foi realizado com sucesso!! ")


            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUE
            )
        
        elif opcao =="3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao =="6":
            listar_contas(contas)  

        elif opcao == "7":
            break

        else:
            print("operação inválida, por favor selecione novamente a operação desejada")  

main()


    
       
