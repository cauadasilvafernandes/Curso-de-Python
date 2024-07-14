
entrada = input("Digite a velocidade do carro em KM/h:") 

numerico = entrada.split()[0] # Separar a parte numérica da unidade

velocidade = float(numerico) # Converter a parte numérica para float

if velocidade > 80:
      excesso = velocidade - 80
      multa = velocidade * 7.00

      print(f"VOCÊ FOI MULTADO! Por estar na velocidade: {velocidade:.2f} KM/h")
      print(f"Valor da multa: R$ {multa:.2f}")
else:
      print("Velocidade dentro do permitido.")











  
    
