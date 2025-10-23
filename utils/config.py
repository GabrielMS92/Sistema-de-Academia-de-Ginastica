import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    print("========= SISTEMA DE ACADEMIA =========")
    print(" 1 - Relatórios")
    print(" 2 - Inserir Registros")
    print(" 3 - Atualizar Registros")
    print(" 4 - Remover Registros")
    print(" 5 - Sair")
    return input("Escolha uma opção: ")

def menu_entidades():
    """Menu para escolher qual entidade gerenciar (Inserir, Atualizar, Remover)."""
    print("\n--- Gerenciar Entidades ---")
    print(" 1 - Aluno")
    print(" 2 - Instrutor")
    print(" 3 - Voltar ao Menu Principal")
    return input("Escolha a entidade: ")

def menu_relatorios():
    """Menu para os relatórios obrigatórios."""
    print("\n--- Menu de Relatórios ---")
    print(" 1 - Relatório: Alunos e seus Instrutores (JOIN)")
    print(" 2 - Relatório: Quantidade de Alunos por Instrutor (GROUP BY)")
    print(" 3 - Voltar ao Menu Principal")
    return input("Escolha o relatório: ")