import statistics
import math
from scipy import stats
import numpy
from collections import Counter

array_numeros = []
array_cargo = []
array_funcionario = []

print("\n--- Bem-vindo(a) a calculadora de estatística simples ---" "\nInforme os valores que serão calculados e a operação logo em seguida.Lembre-se de dar enter quando quiser parar de informar números.")

while True:
    num = input("Digite o sálario dos funcionarios: ")
    fun = input("Digite o nome do funcioário: ")
    carg = input("Digite o cargo do funcionário: ")
    if num == "":
        break
    else:
        array_numeros.append(float(num))

    if fun == "":
        break
    else:
        array_funcionario.append(str(fun))

    if carg == "":
        break
    else:
        array_cargo.append(str(carg))

def tabela():
    print("\nNome\t\tCargo\t\tSalário")
    for i in range(len(array_funcionario)):
        print(f"{array_funcionario[i]}\t\t{array_cargo[i]}\t\tR${array_numeros[i]:.2f}")

tabela()
    
print(f"\nValores inseridos: {array_numeros}")

def menu():
    print("\n--- Informe a operação que deseja realizar ---")
    print("1. Média")
    print("2. Moda")
    print("3. Mediana")
    print("4. Sair")

    while True:
        opcao = int(input("\nEscolha uma opção desejada: "))
        
        if opcao == 1:
            media = statistics.mean(array_numeros)
            print(f"A Média é: R${media:.2f}")

        elif opcao == 2:
            moda = statistics.multimode(array_numeros)
            print(f"A Moda é: R${moda}")

        elif opcao == 3:
            mediana = statistics.median(array_numeros)
            print(f"A Mediana é: R${mediana:.2f}")

        elif opcao == 4:
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida.")

menu()
        
        