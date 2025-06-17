kwh = float(input("Digite a quantidade de kWh consumida: "))
tipo = input("Digite o tipo de instalação (R para residencial, I para industrial, C para comercial): ")

if tipo == "R" or tipo == "r":
    if kwh <= 500:
        preco = kwh * 0.40
    else:
        preco = kwh * 0.65
elif tipo == "I" or tipo == "i":
    if kwh <= 1000:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60
elif tipo == "C" or tipo == "c":
    if kwh <= 5000:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60

if preco > 0:
    print (f"O valor a ser pago será: R${preco}")