numero1 = float(input("Digite um número:"))
numero2 = float(input("Digite um número: "))
numero3 = float(input("Digite um número: "))

numeros = [numero1, numero2, numero3]

maior = max(numeros)
menor = min(numeros)

print(f"O menor número: {menor:.0f}")
print(f"O maior número: {maior:.0f}")