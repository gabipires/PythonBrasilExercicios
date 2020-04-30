peso = float(input("Informe o peso dos peixes pescados (em kg):"))
multa = 4.0
peso_maximo = 50.0

if (peso > peso_maximo):
    excesso = peso - peso_maximo
    print("Excesso de peso:", excesso, "kg")
    print("Valor da multa por excesso R$", excesso * multa)
else:
    print("Não houve excesso de peso!")