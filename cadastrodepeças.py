# Sistema de Cadastro de Peças com Compra e Exclusão

# Lista para armazenar as peças
pecas = []

# Função para adicionar uma peça
def adicionar_peca():
    nome = input("Digite o nome da peça: ")
    codigo = input("Digite o código da peça: ")
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: R$ "))
    
    peca = {
        'nome': nome,
        'codigo': codigo,
        'quantidade': quantidade,
        'preco': preco
    }
    pecas.append(peca)
    print("Peça cadastrada com sucesso!")

# Função para listar as peças cadastradas
def listar_pecas():
    if len(pecas) == 0:
        print("Nenhuma peça cadastrada.")
    else:
        print("\n--- Lista de Peças Cadastradas ---")
        for peca in pecas:
            print(f"Nome: {peca['nome']}, Código: {peca['codigo']}, Quantidade: {peca['quantidade']}, Preço: R$ {peca['preco']:.2f}")

# Função para buscar uma peça pelo código
def buscar_peca():
    codigo = input("Digite o código da peça para buscar: ")
    for peca in pecas:
        if peca['codigo'] == codigo:
            print(f"\n--- Detalhes da Peça ---")
            print(f"Nome: {peca['nome']}")
            print(f"Código: {peca['codigo']}")
            print(f"Quantidade: {peca['quantidade']}")
            print(f"Preço: R$ {peca['preco']:.2f}")
            return
    print("Peça não encontrada.")

# Função para comprar uma peça
def comprar_peca():
    codigo = input("Digite o código da peça que deseja comprar: ")
    quantidade_compra = int(input("Digite a quantidade que deseja comprar: "))
    
    for peca in pecas:
        if peca['codigo'] == codigo:
            if peca['quantidade'] >= quantidade_compra:
                peca['quantidade'] -= quantidade_compra
                valor_total = quantidade_compra * peca['preco']
                print(f"Compra realizada com sucesso! Total a pagar: R$ {valor_total:.2f}")
                print(f"Quantidade restante de {peca['nome']}: {peca['quantidade']}")
                return
            else:
                print("Não há estoque suficiente para essa quantidade.")
                return
    print("Peça não encontrada.")

# Função para excluir uma peça
def excluir_peca():
    codigo = input("Digite o código da peça que deseja excluir: ")
    
    for i, peca in enumerate(pecas):
        if peca['codigo'] == codigo:
            pecas.pop(i)
            print(f"Peça com código {codigo} excluída com sucesso!")
            return
    
    print("Peça não encontrada.")

# Função principal com o menu
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Adicionar Peça")
        print("2. Listar Peças Cadastradas")
        print("3. Buscar Peça pelo Código")
        print("4. Comprar Peça")
        print("5. Excluir Peça")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_peca()
        elif opcao == '2':
            listar_pecas()
        elif opcao == '3':
            buscar_peca()
        elif opcao == '4':
            comprar_peca()
        elif opcao == '5':
            excluir_peca()
        elif opcao == '6':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executando o sistema
menu()