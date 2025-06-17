estoque_livro = {
    "Livro do Batman": 20,
    "Livro do homem aranha": 15,
    "Diario de um Banana": 33,
    "Python para Leigos": 5,
}

estoque_fone = {
    "Fone falso": 25,
    "Fone JBL": 30,
    "Fone Gamer": 70,
    "Fone para Academia": 100,
}

estoque_jogos = {
    "Fifa": 15,
    "GTA VI": 70,
    "The Last of Us": 25,
    "Pes 21": 50,
}

def diminuir_fone(produto, quantidade):
    if produto in estoque_fone:
        if estoque_fone[produto] >= quantidade:
            estoque_fone[produto] -= quantidade
            print(f"Venda realizada! Novo estoque de '{produto}': {estoque_fone[produto]}")
        else:
            print(f"Estoque insuficiente. Quantidade disponível de '{produto}': {estoque_fone[produto]}")
    else:
        print("Produto não encontrado no sistema!")

def diminuir_jogos(produto, quantidade):
    if produto in estoque_jogos:
        if estoque_jogos[produto] >= quantidade:
            estoque_jogos[produto] -= quantidade
            print(f"Venda realizada! Novo estoque de '{produto}': {estoque_jogos[produto]}")
        else:
            print(f"Estoque insuficiente. Quantidade disponível de '{produto}': {estoque_jogos[produto]}")
    else:
        print("Produto não encontrado no sistema!")


def diminuir_livro(produto, quantidade):
    if produto in estoque_livro:
        if estoque_livro[produto] >= quantidade:
            estoque_livro[produto] -= quantidade
            print(f"Venda realizada! Novo estoque de '{produto}': {estoque_livro[produto]}")
        else:
            print(f"Estoque insuficiente. Quantidade disponível de '{produto}': {estoque_livro[produto]}")
    else:
        print("Produto não encontrado no sistema!")

def main_jogos():
    produto = input("Digite o nome do produto: ")
    try:
        quantidade = int(input("Digite a quantidade vendida: "))
        if quantidade > 0:
            diminuir_jogos(produto, quantidade)
        else:
            print("A quantidade deve ser um número positivo.")
    except ValueError:
        print("Por favor, digite um número válido para a quantidade.")

def main_livros():
    produto = input("Digite o nome do produto: ")
    try:
        quantidade = int(input("Digite a quantidade vendida: "))
        if quantidade > 0:
            diminuir_livro(produto, quantidade)
        else:
            print("A quantidade deve ser um número positivo.")
    except ValueError:
        print("Por favor, digite um número válido para a quantidade.")

def main_fones():
    produto = input("Digite o nome do produto: ")
    try:
        quantidade = int(input("Digite a quantidade vendida: "))
        if quantidade > 0:
            diminuir_fone(produto, quantidade)
        else:
            print("A quantidade deve ser um número positivo.")
    except ValueError:
        print("Por favor, digite um número válido para a quantidade.")

def menu():
    while True:
        print("\n--- Livraria Senai ---")
        print("1. Comprar Livro")
        print("2. Comprar Fone")
        print("3. Comprar Jogo")
        print("4. Sair do sistema")

        try:
            opcao = int(input("\nO que você deseja comprar? "))
            if opcao == 1:
                print(estoque_livro)
                main_livros()
            elif opcao == 2:
                print(estoque_fone)
                main_fones()
            elif opcao == 3: 
                print(estoque_jogos)
                main_jogos()
            elif opcao == 4:
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Por favor, insira um número válido.")

if __name__ == "__main__":
    menu()