combustivel = input("Qual o tipo do seu combustível (A- Alcool, G- Gasolina): ")
litros = float(input("Quantos litros o senhor vai colocar? "))

if combustivel == "A" or combustivel == "a":
    preco = 1.90
    desconto = 0.03 if litros <= 20 else 0.05
elif combustivel == "G" or combustivel == "g":
    preco = 2.50
    desconto = 0.04 if litros <= 20 else 0.06

else:
    print ("Digite uma opção valída!")
    exit()

valor_total = litros * (preco * (1 - desconto))

print (f"O valor à ser pago será: R${valor_total:.2f}")