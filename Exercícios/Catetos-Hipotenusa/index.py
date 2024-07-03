import math

catetos_opostos = float(input("Digite o comprimento do cateto oposto: "))

catetos_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = math.sqrt(catetos_opostos**2 + catetos_adjacente**2)

print(f"O comprimento da hipotenusa é {hipotenusa:.2f}")
