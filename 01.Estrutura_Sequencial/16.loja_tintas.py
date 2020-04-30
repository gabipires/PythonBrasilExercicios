area = float(input("Quantos metros quadrados devem ser pintados: "))

litros = area/3.0
latas = int(litros/18.0)


if (litros % 18 != 0):
    latas += 1

valor_total= float(latas*80)

print("Você deverá comprar", latas, "lata(s).")
print("O valor total é R$", valor_total)