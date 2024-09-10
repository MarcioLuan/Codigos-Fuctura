"""4. Escreva um programa que peça o salário de 2 pessoas 
e informe qual dos dois é o maior."""
#Entrada
# salario1 = float(input("Informe o salário 1: "))
# salario2 = float(input("Informe o salário 2: "))

# #Processamento e saída
# if salario1 <= 0 or salario2 <= 0:
#     print(f"O salário não pode ser negativo nem zero")
# elif salario2 == salario1:
#     print(f"Os salários são iguais")
# elif salario1 > salario2:
#     print(f"O salário maior é o primeiro")
# elif salario2 > salario1:
#     print(f"O salário maior é o segundo")


"""Questão 12: Escreva um programa que peça a velocidade do motorista e a velocidade
 máxima em uma determinada avenida, e calcule a multa (se houver), sabendo que são pagos:
a) 50 reais se o motorista ultrapassar em até 10km/h a velocidade permitida 
(ex.: velocidade máxima: 50km/h; motorista a 60km/h ou a 56km/h);

b) 100 reais, se o motorista ultrapassar de 11 a 30 km/h a velocidade permitida.

c) 200 reais, se estiver acima de 31km/h da velocidade permitida.   """

#Entrada
velocidade_motorista = float(input("Informe a velocidade do motorista em km/h: "))
velocidade_maxima = float(input("Informe a velocidade máxima permitida da via em km/h: "))

#Procesamento
diferenca = velocidade_motorista - velocidade_maxima
if diferenca <= 0:
    print("Você não pagará multa")
elif diferenca <= 10 and diferenca > 0:
    print(f"Você pagará multa de RS 50,00 pois ultrapassou em {diferenca} km!")
elif diferenca > 10 and diferenca <=30:
    print(f"Você pagará multa de RS 100,00 pois ultrapassou em {diferenca} km!")
elif diferenca >30:
    print(f"Você pagará multa de RS 200,00 pois ultrapassou em {diferenca} km!")
else:
    print("Digite uma opção válida!")





