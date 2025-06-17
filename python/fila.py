senhas = 0
listapar = []
listaimpar = []

while senhas <= 19:
    senhas +=1
    if senhas %2 != 0:
        listaimpar.append(senhas)
    else:
        listapar.append(senhas)

print(f"foram atendidos {len(listaimpar)} pacientes no guiche 1")
print(f"foram atendidos {len(listapar)} pacientes no guiche 2")