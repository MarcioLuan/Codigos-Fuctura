# #Criação de uma classe
# class Pessoa:
    
#     #Definição dos atributos que esse objeto tem
#     def __init__(self, nome, idade):
#         self.nome=nome
#         self.idade=idade

# #Criando um objeto do tipo Pessoa com nome "Luan" e idade 18
# pessoa1= Pessoa ("Luan", 18)


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


#Ex: temos uma grande empresa que tem diversos funcionários, dentre eles programadores

# #Criação da classe mãe
# class Funcionário:
#     def __ini__(self, nome, salario):


#Criação da classe mãe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade

    def falar (self):
        print(f"Olá, meu nome é {self.nome}")

#Criando classe Brasileiro que herda a classe Pessoa, pois brasileiro É UMA Pessoa
class Brasileiro (Pessoa):

    #Lógica para herdar atributos de Pessoa e adicionar o atributo cpf
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade)
        self.cpf= cpf

pessoa1= Brasileiro ("Márcio", 23, 19584316487)
pessoa1.falar()

