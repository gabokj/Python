entrada = float(input("Digite o número que deseja:"))
numero = int(entrada)
impar = 1
validacao = 0
if numero == 2:
    print(f"o numero {numero} é primo!")
if numero == 0:
   print(f"O número {numero} não é válido! Digite um número inteiro positivo.")
if numero == 1:
    print("O número 1 não é primo")
else:
    eh_primo = True
    for divisor in range(3, int(numero** 0.5) + 1, 2):  
        if numero % divisor == 0:
            eh_primo = False
            break
    if eh_primo:
        print(f"O número {numero} é primo!")
    else:
        print(f"O número {numero} não é primo!")

for n in range(1, numero):
        eh_primo_antecessor = True
        if n > 1:
            for divisor in range(2, int(n ** 0.5) + 1, 2):
                if n % divisor == 0:
                    eh_primo_antecessor = False
                    break
            if eh_primo_antecessor:
                print(f"{n} é primo")
        else:
            print(n)