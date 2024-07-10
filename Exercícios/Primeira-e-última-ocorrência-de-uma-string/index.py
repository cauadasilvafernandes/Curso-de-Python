
frase = input("Digite uma frase: ")


frase_maiuscula = frase.upper()

quantidade = frase_maiuscula.count('A')


primeira_posicao = frase_maiuscula.find('A') + 1   


ultima_posicao = frase_maiuscula.rfind('A') + 1 

print(f"A letra 'A' aparece {quantidade} vezes na frase.")
print(f"A primeira ocorrência da letra 'A' está na posição {primeira_posicao}.")
print(f"A última ocorrência da letra 'A' está na posição {ultima_posicao}.")
