area = float(input("Quantos metros quadrados devem ser pintados: "))

litros = (area / 6.0) * 1.1  # 10% de folga
latas = int(litros / 18.0)
galoes = int(litros / 3.6)

# Calculo de latas
if (litros % 18 != 0):
    latas += 1

# Calculo de galões
if (litros % 3.6 != 0):
    galoes += 1

# Calculo misturando latas e galoes
mix_latas = int(litros / 18.0)
mix_galoes = int((litros - (mix_latas * 18.0)) / 3.6)

if ((litros - (mix_latas * 18.0) % 3.6 != 0)):
    mix_galoes += 1

print("Latas:", latas, " -- Valor: R$", latas * 80)
print("Galoes:", galoes, " -- Valor: R$", galoes * 25)
print("Latas:", mix_latas, "e Galões:", mix_galoes, " -- Valor: R$", (mix_latas*80)+(mix_galoes*25))