real = float(input("Quanto de dinheiro você tem na carteira? R$" ))

dolar = real / 5.63
euro = real / 6.06
boliviano = real / 0.81

print(f"Com R${real:.2f} você pode comprar US${dolar:.2f}")
print(f"Com R$ {real:.2f} você pode comprar EU$ {euro:.2f} ")
print(f"Com R$ {real:.2f} você pode comprar BOB$ {boliviano:.2f}")
