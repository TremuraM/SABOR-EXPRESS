import os

# Lista que armazenará os restaurantes cadastrados
restaurantes = []

# Função que limpa o console (Windows ou Unix)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Exibe o cabeçalho com destaque ao nome do sistema
def exibir_menu():
    print("=" * 40)
    print("🍽️  Bem-vindo ao".center(40))
    print("🍝  SABOR EXPRESS".center(40))
    print("=" * 40)
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurantes")
    print("3 - Ativar restaurante")
    print("4 - Sair")
    print("=" * 40)

# Função que cadastra um restaurante com nome e categoria
def cadastrar_restaurante():
    nome = input("Digite o nome do restaurante: ").strip()
    if nome == "":
        print("❌ Nome inválido.")
        return

    categoria = input("Digite a categoria (ex: Pizza, Sushi, etc.): ").strip()
    if categoria == "":
        print("❌ Categoria inválida.")
        return

    restaurante = {
        "nome": nome,
        "categoria": categoria,
        "ativo": False
    }

    restaurantes.append(restaurante)
    print(f"✅ Restaurante '{nome}' cadastrado com sucesso!")

# Lista todos os restaurantes com nome, categoria e status
def listar_restaurantes():
    if not restaurantes:
        print("📭 Nenhum restaurante cadastrado.")
        return

    print("\n📋 Lista de restaurantes:")
    for i, r in enumerate(restaurantes, start=1):
        status = "🟢 Ativo" if r["ativo"] else "🔴 Inativo"
        print(f"{i}. {r['nome']} ({r['categoria']}) - {status}")

# Ativa um restaurante selecionado pelo número na lista
def ativar_restaurante():
    listar_restaurantes()

    if not restaurantes:
        return

    try:
        indice = int(input("Digite o número do restaurante para ativar: "))
        if 1 <= indice <= len(restaurantes):
            restaurantes[indice - 1]["ativo"] = True
            print(f"✅ Restaurante '{restaurantes[indice - 1]['nome']}' ativado com sucesso!")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Entrada inválida. Digite um número.")

# Função principal que gerencia o ciclo do programa
def main():
    while True:
        limpar_tela()
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_restaurante()
        elif opcao == "2":
            listar_restaurantes()
        elif opcao == "3":
            ativar_restaurante()
        elif opcao == "4":
            print("👋 Encerrando o programa. Até mais!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

        input("\n🔁 Pressione ENTER para voltar ao menu...")

# Executa o programa
if __name__ == "__main__":
    main()
