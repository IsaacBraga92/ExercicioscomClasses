""" Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, 
a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm. """


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5
        self.idade += 1


Isaac = Pessoa('Isaac', 10, 70, 160)

Isaac.envelhecer()
print(f'Idade de {Isaac.nome} é {Isaac.idade} anos. E sua altura é {Isaac.altura}cm.')
