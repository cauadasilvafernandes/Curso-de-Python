


salario = float(input("Digite o salário do funcionário: R$"))


if salario > 1250.00:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15


novo_salario = salario + aumento


print(f"Salário original: R${salario:.2f}")
print(f"Aumento: R${aumento:.2f}")
print(f"Novo salário: R${novo_salario:.2f}")

