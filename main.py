from func import Sistema

def mostra_menu():
    sistema = Sistema() 
    while True:
        print("\n***********MENU***********")
        print("***********ESTOQUE***********")
        print("ADICIONAR NOVAS ESPECIES AO ESTOQUE [1]")
        print("ESPECIES DISPONÍVEIS NO ESTOQUE [2]")
        print("***********FINANCEIRO***********")
        print("VALOR TOTAL DA COMPRA DE UMA ESPECIE [3]")
        print("VALOR DO BUQUE [4]")
        print("***********CLIENTES***********")
        print("CADASTRAR UM NOVO CLIENTE [5]")
        print("CLIENTES CADASTRADOS [6]")
        print("EXCLUIR CADASTRO DE CLIENTE [7]")
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
            sistema.cadastro_cliente ("João", "123456789", 30, "joao@example.com")
            sistema.cadastro_cliente ("Maria", "987654321", 25, "maria@example.com")
            sistema.cadastro_cliente ("Carlos", "456123789", 35, "carlos@example.com")
            sistema.cadastro_cliente ("Ana", "789456123", 28, "ana@example.com")
            sistema.cadastro_cliente ("Lucas", "321654987", 40, "lucas@example.com")
            sistema.cadastro_cliente ("Fernanda", "654789321", 22, "fernanda@example.com")
            sistema.cadastro_cliente ("Ricardo", "987123456", 33, "ricardo@example.com")
            sistema.cadastro_cliente ("Camila", "123789456", 27, "camila@example.com")
            sistema.cadastro_cliente ("Rafael", "456987123", 29, "rafael@example.com")
            sistema.cadastro_cliente ("Juliana", "789321654", 31, "juliana@example.com")
        elif opcao == '6':
            sistema.clientes_cadastrados() 
        elif opcao == '7':
            sistema.exclui_cliente() #NÂO EXISTE AINDA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        elif opcao == '7':
            print("Saindo do sistema...")
            break
        else:
            print("Opcao inválida, tente novamente")

if __name__== "__main__":
    
    mostra_menu()

    