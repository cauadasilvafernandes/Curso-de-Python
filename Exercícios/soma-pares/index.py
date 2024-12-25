soma = 0 
cont = 0 
for  i in range(1, 7):
    num = int(input(f'Digite {i} valor:'))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você colocou {cont} números e a  soma foi {soma}')