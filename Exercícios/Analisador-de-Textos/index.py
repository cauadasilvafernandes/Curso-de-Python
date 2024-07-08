
nome_completo = input("Digite seu nome:")

nome_maiusculo = nome_completo.upper()

nome_minuscula = nome_completo.lower()

quantidade_letras = len(nome_completo.replace(" " , ""))

primeiro_nome = nome_completo.split()[0]

print(f"Nome maiúsculas: {nome_maiusculo}")
print(f"Nome minúsculas:{nome_minuscula}")
print(f"Quantidade de letras:{quantidade_letras}")
print(f"Quantidade de letras no primeiro nome:{primeiro_nome}")