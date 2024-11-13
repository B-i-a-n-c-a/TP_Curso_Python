from func import Sistema

def mostra_menu():
    sistema = Sistema() 
    while True:
        print("\n***********MENU***********")
        print("ADICIONAR NOVAS ESPECIES AO ESTOQUE [1]")
        print("ESPECIES DISPONÍVEIS NO ESTOQUE [2]")
        print("VALOR TOTAL DA COMPRA DE UMA ESPECIE [3]")
        print("VALOR DO BUQUE [4]")
        print("SAIR [5]")
        opcao = input("Informe o número correspondente a opcao que deseja:")
        if opcao == '1':
            sistema.adiciona_flor("Rosa", 25, 5)
            sistema.adiciona_flor("Girassol", 25, 3)
            sistema.adiciona_flor("Lirio", 25, 8)
            sistema.adiciona_flor("Tulipa", 25, 5)
            sistema.adiciona_flor("Orquidea", 25, 15)
            sistema.adiciona_flor("Margarida", 25, 2)
            sistema.adiciona_flor("Hortensia", 25, 16)
            sistema.adiciona_flor("Romelia", 25, 20)
            sistema.adiciona_flor("Suculenta", 25, 5)
            sistema.adiciona_flor("Estrelicia", 25, 15)
            sistema.adiciona_flor("Peonia", 25, 18)

        elif opcao == '2':
            sistema.imprime_estoque()
        elif opcao == '3':
            sistema.compra_por_flor() 
        elif opcao == '4':
            sistema.venda_buque() 
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opcao inválida, tente novamente")

if __name__== "__main__":
    
    mostra_menu()

    