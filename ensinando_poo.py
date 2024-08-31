class Animal:
    def __init__ (self, nome, idade, nro_patas):
        self.nome= nome
        self.idade= idade
        self.nro_patas= nro_patas

    #Criação de uma função para mostrar informações dos pets
    def mostrar_informações(self):
        print(f"O animal {self.nome} tem {self.idade} anos e {self.nro_patas} patas.")

    #Criação da função fazer som
    def fazer_som(self):
        print ("AAAAAAAAAAAAAAAAAA")

#Criação dos objetos
cachorro1= Animal("Bob", 5, 3)
gato1 = Animal ("Robiscreuza", 4, 4)
dinossauro1 = Animal ("Rex", 4000000, 4)
rato1 = Animal ("Xaropinho", 50, 4)
leao1= Animal ("Leo", 20, 4)
capivara1 = Animal ("Maju", 5, 4)

# print(f"O animal {cachorro1.nome} tem {cachorro1.idade} anos e {cachorro1.nro_patas} patas.")
# print(f"O animal {gato1.nome} tem {gato1.idade} anos e {gato1.nro_patas} patas.")
# print(f"O animal {dinossauro1.nome} tem {dinossauro1.idade} anos e {dinossauro1.nro_patas} patas.")
# # print(f"O animal {rato1.nome} tem {rato1.idade} anos e {rato1.nro_patas} patas.")
# # print(f"O animal {leao1.nome} tem {leao1.idade} anos e {leao1.nro_patas} patas.")
# # print(f"O animal {capivara1.nome} tem {capivara1.idade} anos e {capivara1.nro_patas} patas.")

# #utilização dos métodos para os animais
# cachorro1.mostrar_informações()
# gato1.mostrar_informações()
# dinossauro1.mostrar_informações()
# rato1.mostrar_informações()
# leao1.mostrar_informações()
# capivara1.mostrar_informações()

# #Utilização do método fazer_som para os animais
# cachorro1.fazer_som()
# gato1.fazer_som()
# dinossauro1.fazer_som()
# rato1.fazer_som()
# leao1.fazer_som()
# capivara1.fazer_som()






