import time
import sys

print("\n==== Calculadora de Peso ====")
nome = input("\nQual o seu Nome: ")
Peso = input("Qual o seu Peso: ")

def progress_bar(total=20):
    for i in range(total + 1):
        percent = int((i / total) * 100)
        bar = '█' * i + '-' * (total - i)
        sys.stdout.write(f'\r[{bar}] {percent}%')
        sys.stdout.flush()
        time.sleep(0.1)
    print("\nFinalizado!")

progress_bar()

print(f"\nOlá {Peso} seu peso é: {nome}")