from conexion import criar_conexao
from model.aluno import Aluno
from controller.controller_instrutor import ControllerInstrutor
import oracledb # Importar o driver

class ControllerAluno:
    
    def __init__(self):
        pass

    # A função get_next_id() não é necessária

    def inserir_aluno(self, aluno: Aluno) -> Aluno:
        conexao = None
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()
            
            # Pega o ID do instrutor a partir do objeto
            id_instrutor = aluno.get_instrutor().get_id_instrutor() if aluno.get_instrutor() else None
            
            # Cria uma variável Oracle para receber o ID de retorno
            novo_id_var = cursor.var(oracledb.NUMBER)
            
            query = """
                INSERT INTO Alunos (nome, email, id_instrutor_responsavel) 
                VALUES (:1, :2, :3)
                RETURNING id_aluno INTO :4
            """
            valores = (aluno.get_nome(), aluno.get_email(), id_instrutor, novo_id_var)
            
            cursor.execute(query, valores)
            
            # Pega o ID retornado
            novo_id = novo_id_var.getvalue()[0]
            
            conexao.commit()
            
            print("Aluno inserido com sucesso!")
            
            # Retorna um novo objeto Aluno com o ID correto
            return Aluno(novo_id, aluno.get_nome(), aluno.get_email(), aluno.get_instrutor())

        except Exception as e:
            print(f"Erro ao inserir aluno: {e}")
            if conexao:
                conexao.rollback()
            return None
        finally:
            if conexao:
                cursor.close()
                conexao.close()

    def listar_alunos(self) -> list[Aluno]:
        alunos = []
        conexao = None
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()
            
            # Query com JOIN (padrão SQL, funciona em Oracle)
            query = """
                SELECT a.id_aluno, a.nome, a.email, a.id_instrutor_responsavel, i.nome, i.especialidade
                FROM Alunos a
                LEFT JOIN Instrutores i ON a.id_instrutor_responsavel = i.id_instrutor
                ORDER BY a.nome
            """
            cursor.execute(query)
            
            resultados = cursor.fetchall()
            
            for resultado in resultados:
                instrutor = None
                # Se houver um instrutor (resultado[3] não é Nulo)
                if resultado[3] is not None:
                    # Cria o objeto instrutor (usando os dados do JOIN)
                    from model.instrutor import Instrutor
                    instrutor = Instrutor(id_instrutor=resultado[3], nome=resultado[4], especialidade=resultado[5])
                
                aluno = Aluno(id_aluno=resultado[0], nome=resultado[1], email=resultado[2], instrutor=instrutor)
                alunos.append(aluno)
                
            return alunos

        except Exception as e:
            print(f"Erro ao listar alunos: {e}")
            return []
        finally:
            if conexao:
                cursor.close()
                conexao.close()

    def atualizar_aluno(self, aluno: Aluno):
        conexao = None
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()
            
            id_instrutor = aluno.get_instrutor().get_id_instrutor() if aluno.get_instrutor() else None
            
            query = """
                UPDATE Alunos 
                SET nome = :1, email = :2, id_instrutor_responsavel = :3 
                WHERE id_aluno = :4
            """
            valores = (aluno.get_nome(), aluno.get_email(), id_instrutor, aluno.get_id_aluno())
            
            cursor.execute(query, valores)
            conexao.commit()
            
            print("Aluno atualizado com sucesso!")

        except Exception as e:
            print(f"Erro ao atualizar aluno: {e}")
            if conexao:
                conexao.rollback()
        finally:
            if conexao:
                cursor.close()
                conexao.close()

    def remover_aluno(self, id_aluno: int) -> bool:
        conexao = None
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()
            
            query_delete = "DELETE FROM Alunos WHERE id_aluno = :1"
            cursor.execute(query_delete, (id_aluno,))
            conexao.commit()
            
            if cursor.rowcount > 0:
                print("Aluno removido com sucesso!")
                return True
            else:
                print("Aluno não encontrado.")
                return False

        except Exception as e:
            print(f"Erro ao remover aluno: {e}")
            if conexao:
                conexao.rollback()
            return False
        finally:
            if conexao:
                cursor.close()
                conexao.close()
                
    def get_contagem_registros(self, tabela:str) -> int:
        """Função genérica para contar registros."""
        conexao = None
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()
            
            # Validando o nome da tabela
            if tabela not in ['alunos', 'instrutores']:
                raise ValueError("Nome de tabela inválido")
                
            query = f"SELECT COUNT(1) FROM {tabela}"
            
            cursor.execute(query)
            total = cursor.fetchone()[0]
            return total

        except Exception as e:
            print(f"Erro ao contar registros: {e}")
            return 0
        finally:
            if conexao:
                cursor.close()
                conexao.close()