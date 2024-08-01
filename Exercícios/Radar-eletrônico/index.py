#Escreva um programa que leia a velocidade de um carro.
#  Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#  A multa vai custar R$7,00 por cada Km acima do limite.

velocidade_carro = float(input("Qual a velocidade do carro?"))

limite_velocidade = 80.00
multa = 7.00 

if velocidade_carro > limite_velocidade:
    
    excesso = multa * velocidade_carro

    print(f"MULTADO!, a velocidade {velocidade_carro:.2f} Não é permitida nesta via. Você terá que pagar uma multa de R${excesso:.2f} ")

else:
    print(f"LIBERADO! Dirija com segurança.")











  
    
