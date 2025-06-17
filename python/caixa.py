total = 0

while True:
    codigo = int(input("Digite o código do produto: "))
    quantidade = int(input("Digite a quantidade: "))
    if codigo == 0:
        break
    if codigo == 1:
        total += 0.50*quantidade
    elif codigo == 2:
        total += 1.00*quantidade
    elif codigo == 3:
        total += 4.00*quantidade
    elif codigo == 5:
        total += 7.00*quantidade 
    elif codigo == 9:
        total += 8.00*quantidade 
    else:
        print("Codigo invalido")
       
    print (f"\nO valor a ser pagp será: R${total:.2f}")