

n = int(input("Digite um número inteiro: "))
print("Escolha uma base para conversão: ")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")
opcao = int(input("Sua opção: "))

if opcao == 1:
    print(bin(n)[2:])
elif opcao == 2:
    print(oct(n)[2:])
elif opcao == 3:
    print(hex(n)[2:])
else:
    print("Opção inválida")
