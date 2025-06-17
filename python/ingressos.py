num_salas = (int(input("Digite a quantidade de salas: ")))

vendas = [0]*num_salas

print("\nDigite o número de salas (1 até", num_salas -1, ")onde o ingresso foi vendido")
print("Digite 0 para encerrar os dados\n")


while True:
    sala = int(input("Número da sala: "))
    if sala == 0:
        print("encerrando o sistema...")
        break

    if 1 <= sala <num_salas:
        vendas[sala] += 1
    else:
        print("Sala inválida. Tente novamente.")


print("\nQuantidade de ingressos vendidos por sala:")
total = 0
for i in range(num_salas):
    print(f"Sala {i}: {vendas[i]} ingressos")
    total += vendas[i]

print(f"\nTotal de ingressos vendidos: {total}")
