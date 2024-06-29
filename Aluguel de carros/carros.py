km_percorrido = float(input("Quantos quilômetros foram percorridos? "))

dias_alugados = int(input("Por quantos dias o carro foi alugado? "))

preco_total = (60 * dias_alugados) + (0.15 * km_percorrido)

print("O preço total a pagar é R$", preco_total)