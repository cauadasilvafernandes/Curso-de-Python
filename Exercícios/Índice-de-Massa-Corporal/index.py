nome = input('Qual o seu nome?')
peso = float(input('Qual o seu peso?(Kg)' ))
altura = float(input('Qual a sua altura? (m)'))
imc = peso / (altura**2)
print(f'{nome}, O IMC  é de {imc:.1f}')

if imc < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print ('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
     print('Obesidade Mórbida')