lista = [1, 2, 3, 4]
print("\n Impresso antes do erro!\n")
print(lista[4])
print("Essa linha é depois do erro")
















try:
    lista = [1, 2, 3, 4]
    print("\n Impresso antes do erro!\n")
    print(lista[4])
    print("Essa linha é depois do erro")
except IndexError as error:
    print ("O índice solicitado não existe nessa lista")

print(error)