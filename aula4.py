# #Gerando uma sequência de 0 a 9
# print(list(range(10)))

# #Gerando uma sequência de 1 a 10
# print(list(range(1, 11)))

# #Gerando uma sequência de 0  a 30, com step 5
# print(list(range(0, 30, 5)))

# #Gerando uma sequ
# ência numérica negativa
# print(list(range(0, -10, -1)))

# for i in range (1, 6):
#     print(i)


# i = 1
# while i <= 5:
#     print(i)
#     #Adicionando 1 ao valor de i
#     i += 1

# Criando um loop utilizando o for

# for i in range(0, 4):
#     produto = input("Digite o nome do produto: ")
#     valor = float(input("Digite o valor do produto: "))

#Percorrendo lista de numeros
for elemento in [ 1, 2, 3, 4, 5, 6]:
    print (f"Estamos no elemento {elemento}")

#Percorrendo uma String:
for letra in "Melancia":
    print(f"Estamos na letra: {letra}")

#Percorrendo os índices de uma String:
for elemento in range(len("String")):
    print(f"Estamos na letra de numero {elemento}")

#Iterar sobre uma lista de números e calcular a soma:
numeros = [1, 2, 3, 4, 5]
soma = 0
for numero in numeros:
    soma += numero   #Também poderia ser soma = soma + numero
print (soma)

#Ite

