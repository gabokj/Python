deposito = float(input("Digite o valor do depósito inicial: R$ "))
taxa_juros = float(input("Digite a taxa de juros mensal (%): ")) / 100
valor_deposito_mensal = float(input("Digite o valor do depósito mensal: R$ "))

total_juros = 0
saldo = deposito

print("\nMês a mês:")
print("-" * 40)
print("Mês\tSaldo\t\tJuros")
print("-" * 40)

for mes in range(1, 25):
    if mes == 1:
        saldo += valor_deposito_mensal
    juros = saldo * taxa_juros
    total_juros += juros
    saldo += juros
    
    print(f"{mes}\tR$ {saldo:.2f}\tR$ {juros:.2f} \tR$ {valor_deposito_mensal:.2f}")

print("-" * 40)
print(f"\nTotal ganho com juros no período: R$ {total_juros:.2f}")
