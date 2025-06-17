lista = [1, 2, 3, 4]
lista2 = [4, 5, 6]

#set converte a lista em conjuntos 
conjuto = set(lista) 
conjuto2 = set(lista2)

elementos_iguais = conjuto.intersection(conjuto2) #serve para fazer mostrar os elementos em comum de duas listas
elementos_diferentes = conjuto.difference(conjuto2) #serve para fazer a diferença de duas listas
elementos_diferentes2 = conjuto2.difference(conjuto)
elementos_total = conjuto.symmetric_difference(conjuto2) #serve para fazer a diferença total entre as listas

print(f"\nOs elementos em comum são {elementos_iguais}")
print(f"Os elementos diferente da primeira lista são {elementos_diferentes}")
print(f"Os elementos diferente da segunda lista são {elementos_diferentes2}")
print(f"Os elementos diferentes no total são {elementos_total}")
print(f"\nTodos os elementos são {conjuto} e {conjuto2}")