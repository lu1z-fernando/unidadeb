class Carro:
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.vendido = False

    def exibir_informacoes(self):
        status_venda = "Vendido" if self.vendido else "Não vendido"
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Preço: R${self.preco}")
        print(f"Status: {status_venda}")
        print("------------------------")

    def vender(self):
        self.vendido = True

    def ajustar_preco(self, novo_preco):
        self.preco = novo_preco

carro1 = Carro("Toyota", "Corolla", 2022, 80000)
carro2 = Carro("Ford", "Mustang", 2023, 100000)
carro3 = Carro("BMW", "X5", 2021, 120000)
carro4 = Carro("Honda", "Civic", 2022, 75000)
carro5 = Carro("Chevrolet", "Cruze", 2023, 85000)

carro1.exibir_informacoes()
carro2.exibir_informacoes()
carro3.exibir_informacoes()
carro4.exibir_informacoes()
carro5.exibir_informacoes()

carro1.vender()
carro4.ajustar_preco(72000)

carro1.exibir_informacoes()
carro4.exibir_informacoes()

