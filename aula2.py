
# Verdadeiro ou falso?

print (6 % 2 == 0 and 6 % 3 == 0)

print (18 % 5 == 0 or 16 % 4 == 0)

print (5 % 5 == 0 and 5 % 3 == 0)

#Solicitando o cupom
# cupom = input ("Informe o cupom: ")

#Conferindo o cupom
# if cupom == "FUCTURA1":
#     print (f"Você ganhou 15% de desconto!")

# elif cupom == "FUCTURA2":
#     print (f"Você ganhou 10% de desconto!")

# else:
#     print (f"Você ganhou 5% de desconto!")



salario = float(input("Informe o seu salário"))
emprestimo = float(input("Informe o empréstimo desejado"))

if emprestimo <= 0.5 * salario:
    print("Empréstimo aprovado")
elif emprestimo <= 0.75 * salario:
    print("Emprestimo em análise")
else:
    print("Emprestimo não aprovado")