menu = """ 

[1] deposito
[2] saque
[3] extrato
[4] sair

=> """

saldo = 0
limite = 500
extrato =""
numero_saque =0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "1":

        valor = float(input("informe o valor de depósito: "))
        print(f"Valor de R$ {valor:.2f} foi depositado com sucesso!")

        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Valor Inválido!! Por favor informar valor correto")    

    elif opcao == "2":
        
        valor  = float (input("informe o valor do saque: "))
        print(f"Saque de R${valor:.2f} foi realizado com sucesso!! ")
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUE
        
        if excedeu_saldo:
            print("Saldo insuficiente! Por favor tente novamente!")

        elif excedeu_limite:    
            print("Limite Excedido!! Por favor tente novamente!!")

        elif excedeu_saques: 
            print("Ops!! Você excedeu o seu limite de saques diário, por favor Tente amanhã")  

        elif  valor > 0:
           saldo -= valor 
           extrato += f"Saque: R$ {valor:.2f}\n"
           numero_saque +=1

        else: 
            print("Ops! O valor informado é inválido!! Por favor informe o valor correto!!")   
    



    elif opcao =="3":

        print("\n##############EXTRATO##############")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("######################################")
    
    elif opcao == "4":
        print("Obrigado pela preferência!!! Volte Sempre!!!")
        break
     

    else:
        print("Opção Inválida, por favor, selecione novamente a operação correta!!")    
