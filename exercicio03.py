# Classe Retangulo: Crie uma classe que modele um retangulo:
#
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, comp, larg):
        self.comp = comp
        self.larg = larg

    def mudar_comp(self, novo_comp):
        self.comp = novo_comp

    def mudar_larg(self, novo_larg):
        self.larg = novo_larg

    def mostrar_lados(self):
        print(self.comp, self.larg)

    def calcular_area(self):
        area = self.larg * self.comp
        return area

    def calcular_perimetro(self):
        perimetro = self.larg*2 + self.comp*2
        return perimetro


retangulo = Retangulo(3,8)

l = float(input('Informe a largura do local: '))
c = float(input('Informe o comprimento do local: '))

local = Retangulo(c, l)

print(f'Area = {local.calcular_area()} Perimetro = {local.calcular_perimetro()}')