# Classe Bola: Crie uma classe que modele uma bola:
#
# a. Atributos: Cor, circunferência, material
# b. Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self):
        self.cor = 'verde'
        self.circunferencia = 3
        self.material = 'Plastico'

    def mostrar_cor(self):
        return id(self)

    def trocar_cor(self, cor):
        self.cor = cor
