# # #Sabemos a quantidade de vezes que o programa deve ser repetido
# for i in range (5):
#     print ("Oiii")

# while True:
#     print("Não explode por favor")
#     break

# soma=0

# for i in range (5):
#     numero= int(input("Informe um número: "))
#     soma= soma+ numero
#     print(f"O valor da soma é {soma}")

# def print_infos (nome , salario):
#     print(f"O nome é {nome}")
#     print(f"O salário é {salario}")

# print_infos("Luan", 5.111)
# print_infos("Diogenes",50000000000)
# print_infos("Marcos", 60)

# def print_erro():
#     print("Deu erro")
    

# print_erro()

def operacao_x(x, y, z):
    resultado= x + y + z
    return resultado

def operacao_y (x, y, z):
    resultado= x - y - z
    return resultado 

while True:
    try:
        valor1= int(input("Informe o valor 1: "))
        break
    except ValueError:
        print("Você informou uma opção inválida")

while True:
    try:
        valor2= int(input("Informe o valor 2: "))
        break
    except ValueError:
        print("Você informou uma opção inválida")

while True:
    try:
        valor3= int(input("Informe o valor 3: "))
        break
    except ValueError:
        print("Você informou uma opção inválida")

soma= operacao_x(valor1, valor2, valor3)
subtracao= operacao_y(valor1, valor2, valor3)

print(f"a soma é: {soma}")
print(f"a subtracao é: {subtracao}")




