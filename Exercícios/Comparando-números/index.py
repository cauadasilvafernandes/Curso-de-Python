
import os


os.system('cls' if os.name == 'nt' else 'clear')


print("\033[32mVamos fazer um programa de conversor de números!\033[m")


while True:
    nome = input("Qual é o seu nome? ")
    if nome.replace(" ", "").isalpha():  
        break
    print("Por favor, insira um nome válido sem números ou caracteres especiais.")


print(f"Olá, {nome}! Agora vamos comparar dois números.")


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))


if num1 > num2:
    print(f"{nome}, o número {num1} é maior que o número {num2}.")
elif num1 < num2:
    print(f"{nome}, o número {num2} é maior que o número {num1}.")
else:
    print(f"{nome}, os dois números são iguais.")
