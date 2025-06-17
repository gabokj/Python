lista = ["banana", "Morango", "Laranja"]
lista2 = []
print("Lista original:", lista)

while True:
    novo_item = input("Digite uma fruta para adicionar (ou de enter para terminar): ")
    if novo_item == "":
        print("Saindo do sistema...")
        break

    lista2.append(novo_item)

lista_atualizada = lista + lista2
print("Lista atualizada:", lista_atualizada)
