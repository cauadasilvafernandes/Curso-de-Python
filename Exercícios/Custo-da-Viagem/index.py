#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#  Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km 
# e R$0,45 parta viagens mais longas.

distancia = float(input("Qual a distância da sua viajem?"))
print(f"Você vai fazer uma viajem de {distancia:.2f} km.")

tarifa_curta = 0.50 
tarifa_longa = 0.45 

if distancia < 200: 
  passagem =   distancia * tarifa_curta

else:
  passagem =   distancia * tarifa_longa

print(f"O preço da passagem para viajem de {distancia:.2f} km é {passagem:.2f}")
