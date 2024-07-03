import math

ag = float(input("Digite o ângulo em graus:"))
ar = math.radians(ag)

seno = math.sin(ar)
cosseno = math.cos(ar)
tangente = math.tan(ar)

print(f"O angulo de {ag} graus tem:")
print(f"Seno: {seno:.4f}")
print(f"Cosseno: {cosseno:4f}")
print(f"Tangente: {tangente:4f}")