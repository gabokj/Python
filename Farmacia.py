remedios = []

def adicionar_remedios():
    nome = input("Digite o nome do remédio: ")
    principio_ativo = input("Digite o Pincipio ativo: ")
    codigo = input("Digite o codigó do produto: ")
    quantidade = input ("Digite a quantidade: ")
    setor = input ("Digite o setor aonde fica armazenado o remédio: ")
    preco = float(input("Digite o preço: R$"))

    remedio = {    
    'nome': nome,
    'principio_ativo': principio_ativo,
    'codigo': codigo,
    'quantidade': int(quantidade),
    'setor': setor,
    'preco': preco
    }
    remedios.append(remedio)
    print("Remédio cadastrado com sucesso!")

def listar_remedios():
    if len(remedios) == 0:
        print("Nenhum remédio encontrado.")
    else:
        print("\n=== Lista de Remédios Cadastrados ===")
        for remedio in remedios:
            print(f"Nome: {remedio['nome']} ")
            print(f"Principio Ativo: {remedio['principio_ativo']} ")
            print(f"Código: {remedio['codigo']} ")
            print(f"Quantidade: {remedio['quantidade']} ")
            print(f"Setor: {remedio['setor']} ")
            print(f"Preço: R$ {remedio['preco']} ")


def buscas_remedios():
    codigo = input("Digite o codigó do remédio: ")
    for remedio in remedios:
        if remedio['codigo'] == codigo:
            print(f"\n--- Detalhes do Remédio ---")
            print(f"Nome: {remedio['nome']}")
            print(f"Nome: {remedio['principio_ativo']}, ")
            print(f"Código: {remedio['codigo']}")
            print(f"Quantidade: {remedio['quantidade']}")
            print(f"Setor: {remedio['setor']}, ")
            print(f"Preço: R$ {remedio['preco']:.2f}")
            return
    
    print("Remédio não encontrado.")

def comprar_remedios():
    codigo = input("Digite o codigó do remédio: ")
    quantidade_compra = int(input("Digite a quantidade que deseja comprar: "))

    for remedio in remedios:
        if remedio['codigo'] == codigo:
            if remedio['quantidade'] >= quantidade_compra:
                remedio['quantidade'] -= quantidade_compra
                valor = quantidade_compra* remedio['preco']
                print(f"Total a pagar: R$ {valor:.2f}")
                print(f"Compra realizada com sucesso!")
                print(f"\nQuantidade restante de {remedio['nome']}: {remedio['quantidade']}")
            else:
                print("Não há estoque o suficiente para essa quantidade.")
                return
    print("Remédio não encontrado.")

def excluir_remedios():
    codigo = input("Digite o codigó do remédio: ")

    for i, remedio in enumerate(remedios):
        if remedio['codigo'] == codigo:
            remedios.pop(i)
            print(f"Remédio com código {codigo} excluída com sucesso!")
            return
    
    print("Remédio não encontrado.")

def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Adicionar Remédio")
        print("2. Listar Remédio")
        print("3. Buscar Remédio")
        print("4. Comprar Remédio")
        print("5. Excluir Remédio")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_remedios()

        elif opcao == '2':
            listar_remedios()

        elif opcao == '3':
            buscas_remedios()

        elif opcao == '4':
            comprar_remedios() 

        elif opcao == '5':
            excluir_remedios()
        
        elif opcao == '6':
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")


menu()

