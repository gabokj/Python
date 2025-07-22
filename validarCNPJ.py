from validate_docbr import CNPJ

cnpj = CNPJ()

numero = "13604636212" #Exemplo de cnpj

if cnpj.validate(numero):
    print("CNPJ válido! ✅")
else:
    print("CNPJ inválido! ❌")