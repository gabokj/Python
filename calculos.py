a = float(input("digite a velocidade do carro: "))

if a > 80:
    multa = (a - 80) * 5
    print(f"voce foi multado em {multa} reais")
else:
    print("voce nao foi multado")