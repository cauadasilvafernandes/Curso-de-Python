
# Pergunte o valor da casa.
#  o salário do comprador
#  Quantos anos ele vai pagar.
#  A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input("Qual o valor da casa?"))
salario = float(input("Qual é o seu salario mensal?"))
anos = int(input("Quantos anos você pretende pagar?"))

prestacao = casa / (anos * 12 )

limite = salario * 0.3

if prestacao < limite:
    print(f"Empréstimo aprovado! A prestação mensal será R$ {prestacao:2.f} ")
else:
    print(f"Empréstimo negado. A prestação mensal de R$ {prestacao:.2f}  exede 30% do seu salário. ")