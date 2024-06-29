medida = float(input("Digite um número em  metros:"))


km = medida * 1000
hm = medida * 100
dam = medida * 10

print(f"A medida de {medida:.0f}m corresponde a: \n {km:.0f}km \n {hm:.0f}hm \n {dam:.0f}dam")