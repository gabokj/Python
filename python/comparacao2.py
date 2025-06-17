lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 5, 6, 7, 8]
apenaslista1 = []
apenaslista2 = []
iguais = []
diferentes = []

for elemento in lista1:
    if elemento in lista2:
        iguais.append(elemento)
    else:
        diferentes.append(elemento)

for elemento in lista2:
    if elemento not in lista1 and elemento not in diferentes:
        diferentes.append(elemento)

for elemento in lista2:
    if elemento not in lista1:
        apenaslista2.append(elemento)

for elemento in lista1:
    if elemento not in lista2:
        apenaslista1.append(elemento)

print("\nElementos comuns:", iguais)
print("Elementos diferentes:", diferentes)
print("\nElementos apenas na lista 1 são: ", apenaslista1)
print("Elementos apenas na lista 2 são: ", apenaslista2)