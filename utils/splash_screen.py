from utils.config import limpar_tela
from controller.controller_aluno import ControllerAluno
from controller.controller_instrutor import ControllerInstrutor

class SplashScreen:
    def __init__(self):
        # Instancia os controladores para fazer a contagem
        self.ctrl_aluno = ControllerAluno()
        self.ctrl_instrutor = ControllerInstrutor()
        
    def exibir(self):
        limpar_tela()
        
        # 1. Contagem de registros [cite: 28]
        total_alunos = self.ctrl_aluno.get_contagem_registros("alunos")
        total_instrutores = self.ctrl_instrutor.get_contagem_registros("instrutores")

        # 2. Exibição da Splash Screen [cite: 27]
        print("##############################################")
        print("#                                            #")
        print("#         SISTEMA DE ACADEMIA                #")
        print("#                                            #")
        print("##############################################")
        print("\nTOTAL DE REGISTROS EXISTENTES:")
        print(f" 1 - INSTRUTORES: {total_instrutores}")
        print(f" 2 - ALUNOS: {total_alunos}")
        
        print("\nCRIADO POR:")
        print(" - Ricardo Formigoni Souza")
        print(" - Gabriel Moreira da Silva")
        print(" - Addriel Teixeira")
        print(" - Kaio Correia")
        print(" - Lucas Cardozo Machado")
        
        print("\nDISCIPLINA: Banco de Dados")
        print(f"PROFESSOR: {self.get_nome_professor()}") # [cite: 31]
        print("\n##############################################")
        
        input("\nPressione ENTER para continuar...")

    def get_nome_professor(self) -> str:
        # Preserva o nome do professor conforme edital [cite: 3]
        return "Howard Roatti"