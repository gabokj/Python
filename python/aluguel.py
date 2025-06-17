kms = float(input("Digite a quantidade de kms percorridos: "))
dias = int(input("Digite a quantidade de dias: "))

precoD = 60 * dias
precokm = 0.15 * kms

total = precoD + precokm 
print(f"O valor à ser pago será: R${total}")