from utils.config import limpar_tela, menu_principal, menu_entidades, menu_relatorios
from utils.splash_screen import SplashScreen

from reports.relatorios import Relatorios
from controller.controller_instrutor import ControllerInstrutor
from controller.controller_aluno import ControllerAluno
from model.instrutor import Instrutor
from model.aluno import Aluno

# Instanciando objetos globais
splash = SplashScreen()
relatorios_academia = Relatorios()
ctrl_instrutor = ControllerInstrutor()
ctrl_aluno = ControllerAluno()

def run():
    
    # Exibe a Splash Screen inicial
    splash.exibir()
    
    while True:
        limpar_tela()
        opcao_principal = menu_principal()
        
        if opcao_principal == '1':
            # --- Menu de Relatórios ---
            while True:
                limpar_tela()
                opcao_relatorio = menu_relatorios()
                
                if opcao_relatorio == '1':
                    # Relatório de Junção
                    relatorios_academia.executar_relatorio("relatorio_alunos_instrutores.sql")
                elif opcao_relatorio == '2':
                    # Relatório de Agrupamento
                    relatorios_academia.executar_relatorio("relatorio_alunos_por_instrutor.sql")
                elif opcao_relatorio == '3':
                    break # Volta ao menu principal
                else:
                    print("Opção inválida. Tente novamente.")
                
                input("\nPressione ENTER para continuar...")

        elif opcao_principal == '2':
            # --- Inserir Registros ---
            processar_crud(operacao="inserir")

        elif opcao_principal == '3':
            # --- Atualizar Registros ---
            processar_crud(operacao="atualizar")

        elif opcao_principal == '4':
            # --- Remover Registros ---
            processar_crud(operacao="remover")

        elif opcao_principal == '5':
            # --- Sair ---
            print("Saindo do Sistema de Academia. Até logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione ENTER para continuar...")

def processar_crud(operacao: str):
    """Função centralizada para Inserir, Atualizar e Remover."""
    
    while True:
        limpar_tela()
        print(f"--- {operacao.upper()} REGISTROS ---")
        opcao_entidade = menu_entidades()
        
        if opcao_entidade == '1':
            # ALUNO
            if operacao == "inserir":
                inserir_aluno()
            elif operacao == "atualizar":
                atualizar_aluno()
            elif operacao == "remover":
                remover_aluno()
                
        elif opcao_entidade == '2':
            # INSTRUTOR
            if operacao == "inserir":
                inserir_instrutor()
            elif operacao == "atualizar":
                atualizar_instrutor()
            elif operacao == "remover":
                remover_instrutor()
                
        elif opcao_entidade == '3':
            break # Volta ao menu principal
        else:
            print("Opção inválida. Tente novamente.")
            
        # Pergunta se deseja continuar na operação atual
        continuar = input(f"\nDeseja {operacao} mais algum registro? (S/N): ").strip().upper()
        if continuar != 'S':
            break

# Funções de CRUD específicas

def inserir_instrutor():
    print("\n--- Inserir Novo Instrutor ---")
    nome = input("Informe o nome do instrutor: ")
    especialidade = input("Informe a especialidade (ex: Musculação): ")
    
    novo_instrutor = Instrutor(id_instrutor=None, nome=nome, especialidade=especialidade)
    ctrl_instrutor.inserir_instrutor(novo_instrutor)

def inserir_aluno():
    print("\n--- Inserir Novo Aluno ---")
    nome = input("Informe o nome do aluno: ")
    email = input("Informe o email: ")
    
    # Lista instrutores para seleção
    instrutor_selecionado = selecionar_instrutor()
    
    novo_aluno = Aluno(id_aluno=None, nome=nome, email=email, instrutor=instrutor_selecionado)
    ctrl_aluno.inserir_aluno(novo_aluno)

def atualizar_instrutor():
    print("\n--- Atualizar Instrutor ---")
    instrutor_selecionado = selecionar_instrutor(incluir_nenhum=False)
    if not instrutor_selecionado:
        print("Nenhum instrutor selecionado.")
        return
        
    print(f"\nEditando Instrutor: {instrutor_selecionado.to_string()}")
    novo_nome = input(f"Novo nome (Atual: {instrutor_selecionado.get_nome()}): ")
    nova_especialidade = input(f"Nova especialidade (Atual: {instrutor_selecionado.get_especialidade()}): ")
    
    instrutor_selecionado.set_nome(novo_nome)
    instrutor_selecionado.set_especialidade(nova_especialidade)
    
    ctrl_instrutor.atualizar_instrutor(instrutor_selecionado)

def atualizar_aluno():
    print("\n--- Atualizar Aluno ---")
    aluno_selecionado = selecionar_aluno()
    if not aluno_selecionado:
        print("Nenhum aluno selecionado.")
        return
        
    print(f"\nEditando Aluno: {aluno_selecionado.to_string()}")
    novo_nome = input(f"Novo nome (Atual: {aluno_selecionado.get_nome()}): ")
    novo_email = input(f"Novo email (Atual: {aluno_selecionado.get_email()}): ")
    
    print("Selecione o novo instrutor responsável:")
    novo_instrutor = selecionar_instrutor()
    
    aluno_selecionado.set_nome(novo_nome)
    aluno_selecionado.set_email(novo_email)
    aluno_selecionado.set_instrutor(novo_instrutor)
    
    ctrl_aluno.atualizar_aluno(aluno_selecionado)

def remover_instrutor():
    print("\n--- Remover Instrutor ---")
    instrutor_selecionado = selecionar_instrutor(incluir_nenhum=False)
    if not instrutor_selecionado:
        print("Nenhum instrutor selecionado.")
        return

    # Confirmação
    confirmar = input(f"Deseja realmente remover '{instrutor_selecionado.get_nome()}'? (S/N): ").strip().upper()
    if confirmar == 'S':
        # A verificação da FK é feita dentro do controller
        ctrl_instrutor.remover_instrutor(instrutor_selecionado.get_id_instrutor())
    else:
        print("Remoção cancelada.")
        
def remover_aluno():
    print("\n--- Remover Aluno ---")
    aluno_selecionado = selecionar_aluno()
    if not aluno_selecionado:
        print("Nenhum aluno selecionado.")
        return

    # Confirmação
    confirmar = input(f"Deseja realmente remover '{aluno_selecionado.get_nome()}'? (S/N): ").strip().upper()
    if confirmar == 'S':
        ctrl_aluno.remover_aluno(aluno_selecionado.get_id_aluno())
    else:
        print("Remoção cancelada.")

# Funções auxiliares de seleção
def selecionar_instrutor(incluir_nenhum=True) -> Instrutor:
    """Lista instrutores e retorna o objeto selecionado."""
    instrutores = ctrl_instrutor.listar_instrutores()
    if not instrutores:
        print("Erro: Não há instrutores cadastrados!")
        return None
        
    print("\nInstrutores Disponíveis:")
    for i, instrutor in enumerate(instrutores):
        print(f" {i+1} - {instrutor.to_string()}")
    
    if incluir_nenhum:
        print(" 0 - Nenhum / Não associar")
    
    while True:
        try:
            escolha = int(input("Selecione o ID (número da lista): "))
            
            if incluir_nenhum and escolha == 0:
                return None
            if 1 <= escolha <= len(instrutores):
                return instrutores[escolha - 1] # Retorna o objeto Instrutor
            else:
                print("Seleção inválida.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def selecionar_aluno() -> Aluno:
    """Lista alunos e retorna o objeto selecionado."""
    alunos = ctrl_aluno.listar_alunos()
    if not alunos:
        print("Erro: Não há alunos cadastrados!")
        return None
        
    print("\nAlunos Cadastrados:")
    for i, aluno in enumerate(alunos):
        print(f" {i+1} - {aluno.to_string()}")
        
    while True:
        try:
            escolha = int(input("Selecione o ID (número da lista): "))
            if 1 <= escolha <= len(alunos):
                return alunos[escolha - 1] # Retorna o objeto Aluno
            else:
                print("Seleção inválida.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

# --- Ponto de Entrada da Aplicação ---
if __name__ == "__main__":
    run()