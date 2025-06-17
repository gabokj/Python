x=1
soma = 0
mensal = 0
print("Rendimento : 0,05% am")
deposito = float(input("Deposito Inicial: "))
deposito_mensal = float(input("Digite o valor que será depositado mensalmente: "))

while x<=24:
    mensal = mensal+deposito_mensal
    soma = soma+((deposito+mensal)*0.005)
    rendimento = soma +deposito + mensal
    investido = deposito+mensal
    x= x+1
    print(f"Mês {x} - Total investido: R${investido:.2f} - Total de juros: R${soma:.2f} - Total acumulado: R${rendimento:.2f}")

print(f"\n == Total investido: R${investido:.2f} - Total de juros: R${soma:.2f} - Total acumulado: R${rendimento:.2f} ==")