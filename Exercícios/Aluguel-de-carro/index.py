km_percorridos = float(input("Digite a quantidade de quilômetros percorridos:"))

dias_alugados = int(input("Digite a quantidade de dias de aluguel:"))

preco_por_dia = 60 
preco_por_km = 0.15 

preco_total = (preco_por_dia) + ( km_percorridos * preco_por_km)

print(f" O preço a pagar pelo aluguel é {preco_total:.2f}") 