valor_hora = float(input("Quanto você ganha por hora: "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês: "))

salario_bruto = valor_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato

print("Salário Bruto: R$", salario_bruto)
print("Imposto de Renda: R$", ir)
print("INSS: R$", inss)
print("Sindicato: R$", sindicato)
print("Salário Liquido: R$", salario_liquido)