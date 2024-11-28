print('========= LOJAS CAUÃ =========')

def calcular_valor():
    print("=== Sistema de Pagamento ===")
    preco = float(input("Digite o preço do produto: R$ "))
    print("""
Escolha a forma de pagamento:
[1] À vista no dinheiro/cheque (10% de desconto)
[2] À vista no cartão (5% de desconto)
[3] Em até 2x no cartão (sem juros)
[4] 3x ou mais no cartão (20% de juros)
    """)
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        valor_final = preco * 0.90
        print(f"O valor a ser pago é R$ {valor_final:.2f} (10% de desconto).")
    elif opcao == 2:
        valor_final = preco * 0.95
        print(f"O valor a ser pago é R$ {valor_final:.2f} (5% de desconto).")
    elif opcao == 3:
        valor_final = preco
        print(f"O valor a ser pago é R$ {valor_final:.2f} (sem desconto).")
        print(f"O pagamento será em 2 parcelas de R$ {valor_final / 2:.2f} cada.")
    elif opcao == 4:
        parcelas = int(input("Digite a quantidade de parcelas (mínimo 3): "))
        if parcelas < 3:
            print("Opção inválida! Para essa condição, o número de parcelas deve ser 3 ou mais.")
        else:
            valor_final = preco * 1.20
            print(f"O valor a ser pago é R$ {valor_final:.2f} (20% de juros).")
            print(f"O pagamento será em {parcelas} parcelas de R$ {valor_final / parcelas:.2f} cada.")
    else:
        print("Opção inválida! Tente novamente.")

# Executa o programa
calcular_valor()

