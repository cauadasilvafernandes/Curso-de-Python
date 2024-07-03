preco = float(input("Digite o preço do produto:"))

desconto = preco * 0.05

novo_preco = preco - desconto 
print(f"O novo preço do produto com 5% de desconto é: R${novo_preco:.2f}")