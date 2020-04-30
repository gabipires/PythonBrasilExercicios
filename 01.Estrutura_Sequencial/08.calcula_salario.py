salario= int(input("Qual o valor da sua hora trabalhada: "))
horas=int(input("Informe a quantidade de horas trabalhadas: "))

total = salario*horas
total = str(total)

print("O seu salário neste mês será: {} reais".format(total))