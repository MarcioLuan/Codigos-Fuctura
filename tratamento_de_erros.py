# lista = [1, 2, 3, 4]
# print("\n Impresso antes do erro!\n")
# print(lista[4])
# print("Essa linha é depois do erro")

# try:
#     lista = [1, 2, 3, 4]
#     print("\n Impresso antes do erro!\n")
#     print(lista[4])
#     print("Essa linha é depois do erro")
# except IndexError as erro:
#     print("O índice solicitado não existe nessa lista")

# print("oiii")

# v1= [4, 8, 16, 32, 64, 128]
# v2= [2, 0, 4, 8, 0]

# #vamos efetuar divisão  entre o v1 por v2

# for i in range(len(v1)):
#     divisao= v1[i]/v2[i]
#     print (f"O resultado de {v1[i]} dividido por {v2[i]} é {divisao}\n")

# v1= [4, 8, 16, 32, 64, 128, 20]
# v2= [2, 0, 4, 8, 0]

# #Laço for para percorrer a lista a quantidade de elementos que tem na lista v1
# for i in range(len(v1)):
#     try:
#         divisao= v1[i]/v2[i]
#         print (f"O resultado de {v1[i]} dividido por {v2[i]} é {divisao}\n")
    
#     #Tratamento do erro da divisão por zero
#     except (ZeroDivisionError):
#         print (f"Não é possível dividir um número por zero\n")
#     #Tratamento do erro de índice da lista
#     except (IndexError):
#         print (f"O índice solicitado não existe nessa lista\n")

# v1= [4, 8, 16, 32, 64, 128, 20]
# v2= [2, 0, 4, 8, 0]

# #Laço for para percorrer a lista a quantidade de elementos que tem na lista v1
# for i in range(len(v1)):
#     try:
#         divisao= v1[i]/v2[i]
#         print (f"O resultado de {v1[i]} dividido por {v2[i]} é {divisao}\n")
    
# #     #Tratamento do erros erros com a mesma mensagem
# #     except (ZeroDivisionError, IndexError):
# #         print (f"Não é possível dividir um número por zero ou indice não existe na lista\n")

# v1= [4, 8, 16, 32, 64, 128, 20]
# v2= [2, 0, 4, 8, 0]

# #Laço for para percorrer a lista a quantidade de elementos que tem na lista v1
# for i in range(len(v1)):
#     try:
#         divisao= v1[i]/v2[i]
#         print (f"O resultado de {v1[i]} dividido por {v2[i]} é {divisao}\n")
    
#     #Tratamento de erros de maneira genérica
#     except:
#         print (f"Deu erro\n")

try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0

except ZeroDivisionError:
    # Código que trata a exceção
    print("Divisão por zero!")
    
finally:
    # Código que será executado sempre
    print("Execução do bloco finally.")