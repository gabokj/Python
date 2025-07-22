from validate_docbr import CPF

cpf = CPF()

numero = "13604636212" #Exemplo de CPF

if cpf.validate(numero):
    print("CPF válido! ✅")
else:
    print("CPF inválido! ❌")