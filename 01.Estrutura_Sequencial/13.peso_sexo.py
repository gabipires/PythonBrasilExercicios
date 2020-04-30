
sexo = input("Informe seu sexo (M/F): ")
altura = float(input("Informe sua altura (em metros): "))
peso = float(input("Informe o seu peso (em kg): "))

if (sexo == "M"):
    peso_ideal = round(((72.7 * altura) - 58),1)
else:
    peso_ideal = round(((62.1 * altura) - 44.7), 1)

if (peso > peso_ideal):
    print("Você está acima do seu peso ideal:", peso_ideal)
elif (peso < peso_ideal):
    print("Você está abaixo do seu peso ideal:", peso_ideal)
else:
    print("Voce está no seu peso ideal:", peso_ideal)