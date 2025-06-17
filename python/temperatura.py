import statistics
T = [ -10, -8, 0, 1, 2, 5, -2, -4]
T.sort()
print(T)
T_menor = (-10)
T_maior = (5)
T_media = statistics.mean(T)
print(f"A menor temperatura é: {T_menor}")
print(f"A maior temperatura é: {T_maior}")
print(f"A média de temperatura é: {T_media}")