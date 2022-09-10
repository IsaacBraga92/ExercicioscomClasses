# Classe Quadrado: Crie uma classe que modele um quadrado:
#   a. Atributos: Tamanho do lado
#   b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def retornar_lado(self):
        print(self.lado)

    def mudar_lado(self, novo_lado):
        self.lado = novo_lado

    def calcular_area(self):
        area = self.lado**2
        print(area)


quadrado = Quadrado(2)

print(quadrado.__dict__)
quadrado.retornar_lado()
quadrado.calcular_area()

quadrado.mudar_lado(4)
print(quadrado.__dict__)
quadrado.retornar_lado()
quadrado.calcular_area()

