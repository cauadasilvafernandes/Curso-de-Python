
from datetime import date

nome = input("Qual o nome do atleta? ")
idade_atleta = int(input("Qual a idade do atleta? "))
nascimento = int(input("Qual o ano de nascimento do atleta? "))

atual = date.today().year
idade = atual - nascimento

print(f"O atleta {nome} tem {idade} anos")

if idade <= 9:
    print("Categoria MIRIM")
elif 10 <= idade <= 14:
    print("Categoria INFANTIL")
elif 15 <= idade <= 19:
    print("Categoria JUNIOR")
elif 20 <= idade <= 25:
    print("Categoria SENIOR")
else:
    print("Categoria MASTER")
