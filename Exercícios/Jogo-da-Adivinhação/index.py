from time import sleep
import random

computador = random.randint(0, 10 )

print('-=-' * 20)
print("Vou pensar em um número 0 e 10. Tente adivinhar.")
print('-=-' * 20)

jogador = int(input("Em que número eu pensei?"))

print("Processando...")
sleep(3)

if jogador == computador:
    print("PARABÉNS!")
else:
    print(f"GANHEI! Eu pensei no número {computador} e não no {jogador}!")
