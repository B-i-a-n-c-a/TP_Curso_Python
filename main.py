from func import Sistema

def mostra_menu():
    sistema = Sistema() 
    while True:
        print("\n***********MENU***********\n\n")
        print("CONTROLE DE ESTOQUE [1]")
        print("FINANCEIRO [2]")
        print("CADASTRO DE CLIENTE [3]")
        print("PROCESSAMENTO DE PEDIDOS [4]")
        print("SAIR [5]")
        opcao = input("Informe o número correspondente a opcao que deseja: \n")
        if opcao == '1':
            sistema.estoque()
        elif opcao == '2':
            sistema.financeiro()
        elif opcao == '3':
            sistema.cadastro_cliente()
        elif opcao == '4':
            sistema.pedidos()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opcao inválida, tente novamente")


if __name__== "__main__":
    
    mostra_menu()
    