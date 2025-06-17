populacao = int(input("Digite a população total do primeiro país: "))
taxadecrescimento = float(input("Digite qual a taxa de crescimento anual do primeiro país: "))

populacao2 = int(input("Digite a população total do segundo país: "))
taxadecrescimento2 = float(input("Digite qual a taxa de crescimento anual do segundo país: "))

crescimento = 0
crescimento2 = 0
anos = 0

taxadecrescimento = 1 + taxadecrescimento / 100
taxadecrescimento2 = 1 + taxadecrescimento2 / 100

while populacao < populacao2:
    populacao *= taxadecrescimento
    populacao2 *= taxadecrescimento2
    anos +=1

print(f"A população se iguala daqui à {anos} anos")
    