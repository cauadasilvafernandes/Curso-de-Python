
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = input("Digite o seu nome completo:")

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
quantidade_letra = len(nome.replace(" " , ""))
primeiro_nome = nome.split()[0]
letras_primeironome = len(primeiro_nome) 

print(f"O nome em maiúsculo fica: {nome_maiusculo}")
print(f"O nome em minúsculo fica: {nome_minusculo}")
print(f"A quantidade de letras no seu nome é: {quantidade_letra}")
print(f"A quantidade de letras do primeiro nome é: {letras_primeironome}")


