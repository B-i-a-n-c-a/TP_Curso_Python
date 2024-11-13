from flor import Flor

class Sistema: 

    def __init__(self):
        self.estoque = []

    def adiciona_flor(self, especie, quantidade, preco):
        flor = Flor(especie, quantidade, preco)
        self.estoque.append(flor)
        print(f"Flor: {flor.especie} | Quantidade: {flor.quantidade} | Preco: {flor.preco} adicionada ao estoque com sucesso!!!")

    def imprime_estoque(self):
        print("***** ESTOQUE *****")
        if not self.estoque:
            print("Estoque vazio!")
        for flores in self.estoque:
            print(f" Especie: {flores.especie} | Quantidade: {flores.quantidade} | Preco: {flores.preco} ")
            print("---------------------------------------------------\n")

    def compra_por_flor(self):
        especie = input("Qual especie deseja calcular o valor da compra? ")
        for flor in self.estoque:
            if flor.especie == especie:
                total = (flor.quantidade * flor.preco)
                print(f"O total da compra de {especie} foi de R$: ", total)
                return True
        print("Especie não encontrada no estoque!")
        return False

    def venda_buque(self):
        tamanho = input("Qual o tamanho do buque?\n[P, M OU G] ")
        especie = input("De qual especie sera o buque: ")
        for especie in self.estoque:
            if tamanho.lower() == "P".lower() and especie in self.estoque:
                total_buque =  ((self.estoque[2].preco + (self.estoque[2].preco / 2)) * 12) + 50
                print("\nO buque tamanho PEQUENO ficou R$ ", total_buque) 
                break
            elif tamanho.lower() == "M".lower() and especie in self.estoque:
                total_buque =  ((self.estoque[2].preco + (self.estoque[2].preco / 2)) * 24) + 50
                print("\nO buque tamanho MEDIO ficou R$ ", total_buque) 
                break
            elif tamanho.lower() == "G".lower() and especie in self.estoque:
                total_buque =  ((self.estoque[2].preco + (self.estoque[2].preco / 2)) * 36) + 50
                print("\nO buque tamanho GRANDE ficou R$ ", total_buque) 
                break
            else:
                print("Tamanho ou especie não identificada!!!")

    def cadastro_cliente(self):
        print("nada ainda cadastro cliente")

    def pedidos(self):
        print("nada ainda pedidos")