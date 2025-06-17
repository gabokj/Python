total = 0
while True:
    codigo = int(input("digite o codigo do produto: "))
    if codigo == 0:
        break
    elif codigo not in [1, 2, 3, 5, 9]:
        print("Código inválido")
        continue
        
    quantidade = int(input("digite a quantidade comprada: "))
    
    if codigo == 1:
        total += 0.50 * quantidade
    elif codigo == 2:
        total += 1.00 * quantidade 
    elif codigo == 3:
        total += 4.00 * quantidade
    elif codigo == 5:
        total += 7.00 * quantidade
    elif codigo == 9:
        total += 8.00 * quantidade

print(f"Total das compras: R$ {total:.2f}")