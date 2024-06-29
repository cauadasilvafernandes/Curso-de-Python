carteira = float(input("Digite quanto dinheiro você tem na carteira? "))

taxadolar = 5.16
taxaeuro = 17.98

euro = carteira / taxaeuro
dolar = carteira / taxadolar

print(f"Com R$ {carteira:.2f} você pode comprar aproximadamente US$: {dolar:.2f}.")
print(f"Com R$ {carteira:.2f} você pode comprar aproximadamente EUR$ {euro:.2f} ")