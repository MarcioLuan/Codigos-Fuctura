# Criação de uma classe
# class Pessoa:

#     #Definição dos atributos que esse objeto tem
#     def __init__(self, nome, idade):
#         self.nome=nome
#         self.idade=idade

# #Criando um objeto do tipo Pessoa com nome "Luan" e idade 18
# pessoa1= Pessoa ("Luan", 18)
# pessoa2= Pessoa ("Márcio", 61)

# #Acessando atributos (quando não são protegidos (veremos outra forma depois):
# print(pessoa1.nome)
# print(pessoa1.idade)
# print(pessoa2.nome)
# print(pessoa2.idade)


# #Criação da classe mãe
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome=nome
#         self.idade=idade

#     #Criação do método falar (sem especificar porque cada nacionalidade
#     #fala uma lingua diferente)
#     def falar ():
#         pass

# #Criando classe Brasileiro que "É UMA PESSOA" então pode herdar
# #Colocar o nome da classe mãe entre parênteses faz com que ela herde os atributos e métodos
# class Brasileiro (Pessoa):

#     #Sobrescrevendo o método falar pois brasileiro fala português
#     def falar (self):
#         print("Olá, meu nome é {self.nome}")

# #Criando classe Espanhol que "É UMA PESSOA" então pode herdar
# class Espanhol(Pessoa):

#     #Sobrescrevendo o método falar pois espanhol fala espanhol
#     def falar(self):
#         print (f"Hola, mi nombre es {self.nome}")


# #Criando um objeto do tipo Brasileiro com nome "Luan" e idade 18 e Espanhol Anderson, idade 20
# pessoa1= Brasileiro ("Luan", 18)
# pessoa2= Espanhol ("Anderson", 20)
# #Fazendo com que o objeto realize o método
# pessoa1.falar()
# pessoa2.falar()


# Ex: temos uma grande empresa que tem diversos funcionários, dentre eles programadores

# #Criação da classe mãe
# class Funcionário:
#     def __ini__(self, nome, salario):


# Criação da classe mãe
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome=nome
#         self.idade=idade

#     def falar (self):
#         print(f"Olá, meu nome é {self.nome}")

# #Criando classe Brasileiro que herda a classe Pessoa, pois brasileiro É UMA Pessoa
# class Brasileiro (Pessoa):

#     #Lógica para herdar atributos de Pessoa e adicionar o atributo cpf
#     def __init__(self, nome, idade, cpf):
#         super().__init__(nome, idade)
#         self.cpf= cpf

# pessoa1= Brasileiro ("Márcio", 23, 19584316487)
# pessoa1.falar()

# class Pessoa:
#     def __init__(self, nome, idade):
#         #Atributo privado
#         self.__nome = nome
#         self._idade = idade

# pessoa1= Pessoa("Joana", 26)

# print(pessoa1.__nome)
# print(pessoa1._idade)


# # class Pessoa:
# #     def __init__(self, nome, idade):
# #         self.__nome = nome
# #         self._idade = idade

# #     def get_nome (self):
# #         return self.__nome

# #     def set_nome (self, novo_nome):
# #         self.__nome = novo_nome

# #     def get_idade(self):
# #         return self._idade

# #     def set_idade(self, nova_idade):
# #         self._idade = nova_idade

# # pessoa1= Pessoa ("Priscila", 26)
# # print(pessoa1.get_nome())      #Obtendo o nome através do método get
# # pessoa1.set_nome("Raphaela")   #Alterando o nome através do método set
# # print(pessoa1.get_nome())      #Obtendo o  novo nome através do método get


# from abc import ABC, abstractmethod
# #Criando a interface
# class Forma(ABC):
#     @abstractmethod
#     def calcular_area():
#         pass

# #Criando classe Retangulo que implementa Forma
# class Retangulo(Forma):
#     def __init__ (self, comprimento, largura):
#         self.comprimento=comprimento
#         self.largura=largura

# #Criando classe Circulo que implementa Forma
# class Circulo(Forma):
#     def __init__(self, raio):
#         self.raio=raio

# circulo1= Circulo(2)

from abc import ABC, abstractmethod


# Criando a interface
class Forma(ABC):
    @abstractmethod
    def calcular_area():
        pass


# Criando classe Retangulo que implementa Forma
class Retangulo(Forma):
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        area = self.comprimento * self.largura
        return area


# Criando classe Circulo que implementa Forma
# class Circulo(Forma):
#     def __init__(self, raio):
#         self.raio = raio

#     def calcular_area(self):
#         area = 3.14 * (self.raio**2)
#         return area


# circulo1 = Circulo(2)
retangulo1 = Retangulo(4, 1.3)
# print(circulo1.calcular_area())
# print(retangulo1.calcular_area())
