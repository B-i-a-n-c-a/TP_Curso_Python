from fornecedor import Fornecedor

class Sistema: 

    dados = Fornecedor()

    def estoque(self):
        print("nada ainda estoque")

    def compra_fornecedor(dados):
        total = (dados.quantidade * dados.preco)
        print("O total da compra de '{dados.especie}' foi de R$: ", total)

    def venda_buque(dados, self):
        tamanho = input("Qual o tamanho do buque?\n[PEQUENO, MEDIO OU GRANDE]")
        especie = input("De qual especie sera o buque:")
        if tamanho == "pequeno" and especie in self.itens:
            total_buque =  ((self.preco + (self.preco/2)) * 12) + 50
            print("O buque tamanho PEQUENO ficou R$: ", total_buque) 
        elif tamanho == "medio" and especie in self.itens:
            total_buque =  ((self.preco + (self.preco/2)) * 24) + 50
            print("O buque tamanho MEDIO ficou R$: ", total_buque) 
        elif tamanho == "grande" and especie in self.itens:
            total_buque =  ((self.preco + (self.preco/2)) * 36) + 50
            print("O buque tamanho GRANDE ficou R$: ", total_buque) 
        else:
            print("Tamanho ou especie não identificada!!!")









    def cadastro_cliente(self):
        print("nada ainda cadastro cliente")


    def pedidos(self):
        print("nada ainda pedidos")