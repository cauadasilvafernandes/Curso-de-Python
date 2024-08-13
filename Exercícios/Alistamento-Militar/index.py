
from datetime import date

def validar_nome():
    while True:
        nome = input("Qual o seu nome? ").strip()
        if not nome:
            print("Você precisa digitar algo.")
        elif not nome.replace(" ", "").isalpha():
            print("O nome deve conter apenas letras.")
        else:
            return nome

def validar_nascimento():
    while True:
        try:
            nascimento = int(input("Em qual ano você nasceu? ").strip())
            if nascimento > date.today().year:
                print("Ano de nascimento inválido.")
            else:
                return nascimento
        except ValueError:
            print("Por favor, digite um ano válido.")

nome = validar_nome()
nascimento = validar_nascimento()

atual = date.today().year
idade = atual - nascimento
idade_alistamento = 18

if idade < idade_alistamento:
    falta = idade_alistamento - idade
    print(f"{nome}, você ainda vai se alistar no serviço militar. Faltam {falta} anos.")
elif idade == idade_alistamento:
    print(f"{nome}, este ano você se alista no serviço militar!")
else:
    anos_passaram = idade - idade_alistamento
    print(f"{nome}, você já passou do tempo de se alistar ao serviço militar!")

