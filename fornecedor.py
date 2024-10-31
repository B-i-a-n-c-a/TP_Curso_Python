class Fornecedor:

    itens = []

    def __init__(self, especie, quantidade, preco):
        self.especie = especie
        self.quantidade = quantidade
        self.preco = preco #preço unitário 

    def adiciona_flor(self, especie, quantidade, preco):
        flor = Fornecedor(especie, quantidade, preco)
        self.itens[especie] = flor

    def imprime_estoque(self):
        for self.especie in self.itens:
            print("| Especie: {self.especie} | Quantidade: {self.quantidade} |\n")
            print("----------------------------------\n")


    #especies e precos usados para testes
    #rosa = 5
    #girassol = 3
    #lirio = 8
    #tulipa = 5
    #orquidea = 15
    #margarida = 2
    #hortensia = 16
    #romelia = 20
    #suculenta = 5
    #estrelicia = 15
    #peonia = 18

