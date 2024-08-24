
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno:"))

media = (nota1 + nota2) / 2

print(f"O aluno que tirou {nota1} e {nota2} Com a média {media}")
 

if media <5.0:
    print("REPROVADO")

elif media >=5.0 and media <=6.9:
    print("RECUPERAÇÃO")

else:
  aprovação =  media >=7.0
  print("APROVADO")
