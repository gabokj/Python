import statistics
import math
from scipy import stats
import numpy
from collections import Counter

func1 = print("Zequinha da Silva, Desenvolvedor JR, R$5.800.00")
func2 = print("Tonho da Silva, Desenvolvedor Pleno, R$7.250.00")
func3 = print("Arliquei da Silva, Desenvolvedor Seniôr, R$9.322.00")
func4 = print("Janderni dos Santos, Desenvolvedor JR, R$5.800.00")
func5 = print("Arismei dos Santos, Desenvolvedor Pleno, R$7.250.00")

salario1 = 5800.00
salario2 = 7250.00
salario3 = 9322.00
salario4 = 5800.00
salario5 = 7250.00

salario = (salario1, salario2, salario3, salario4, salario5)
media = statistics.mean(salario)
print(f"\nMédia: R${media}")


mediana = statistics.median(salario)
print(f"Mediana:  R${mediana}")

moda = statistics.multimode(salario)
print(f"Moda: R${moda}")

