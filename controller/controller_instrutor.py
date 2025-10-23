from conexion import criar_conexao
from model.instrutor import Instrutor
import oracledb # Importar o driver

class ControllerInstrutor:
    
    def __init__(self):
        pass

    def inserir_instrutor(self, instrutor: Instrutor) -> Instrutor:
        conexao = None
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()
            
            # Cria uma variável Oracle para receber o ID de retorno
            novo_id_var = cursor.var(oracledb.NUMBER)
            
            # Query SQL com placeholders Oracle (:1, :2) e cláusula RETURNING
            query = """
                INSERT INTO Instrutores (nome, especialidade) 
                VALUES (:1, :2)
                RETURNING id_instrutor INTO :3
            """
            # Concatenação de atributos (sem ORM)
            valores = (instrutor.get_nome(), instrutor.get_especialidade(), novo_id_var)
            
            cursor.execute(query, valores)
            
            # Pega o ID retornado
            # O getvalue() retorna uma lista, pegamos o primeiro item [0]
            novo_id = novo_id_var.getvalue()[0]
            
            conexao.commit()
            
            print("Instrutor inserido com sucesso!")
            
            # Retorna o instrutor com o ID atualizado
            return Instrutor(novo_id, instrutor.get_nome(), instrutor.get_especialidade())

        except Exception as e:
            print(f"Erro ao inserir instrutor: {e}")
            if conexao:
                conexao.rollback()
            return None
        finally:
            if conexao:
                cursor.close()
                conexao.close()

    def listar_instrutores(self) -> list[Instrutor]:
        instrutores = []
        conexao = None
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()
            
            query = "SELECT id_instrutor, nome, especialidade FROM Instrutores ORDER BY nome"
            cursor.execute(query)
            
            resultados = cursor.fetchall()
            
            for resultado in resultados:
                instrutor = Instrutor(resultado[0], resultado[1], resultado[2])
                instrutores.append(instrutor)
                
            return instrutores

        except Exception as e:
            print(f"Erro ao listar instrutores: {e}")
            return []
        finally:
            if conexao:
                cursor.close()
                conexao.close()

    def atualizar_instrutor(self, instrutor: Instrutor):
        conexao = None
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()
            
            query = """
                UPDATE Instrutores 
                SET nome = :1, especialidade = :2 
                WHERE id_instrutor = :3
            """
            valores = (instrutor.get_nome(), instrutor.get_especialidade(), instrutor.get_id_instrutor())
            
            cursor.execute(query, valores)
            conexao.commit()
            
            print("Instrutor atualizado com sucesso!")

        except Exception as e:
            print(f"Erro ao atualizar instrutor: {e}")
            if conexao:
                conexao.rollback()
        finally:
            if conexao:
                cursor.close()
                conexao.close()

    def remover_instrutor(self, id_instrutor: int) -> bool:
        conexao = None
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()
            
            # 1. Verifica se o instrutor é FK em Alunos (Sintaxe Oracle para LIMIT 1)
            query_check = "SELECT 1 FROM Alunos WHERE id_instrutor_responsavel = :1 FETCH FIRST 1 ROWS ONLY"
            cursor.execute(query_check, (id_instrutor,))
            
            if cursor.fetchone():
                # Se encontrou, não pode excluir
                print(f"Erro: Não é possível remover o instrutor (ID: {id_instrutor}).")
                print("Ele está associado a um ou mais alunos.")
                return False
            
            # 2. Se não é FK, pode remover
            query_delete = "DELETE FROM Instrutores WHERE id_instrutor = :1"
            cursor.execute(query_delete, (id_instrutor,))
            conexao.commit()
            
            if cursor.rowcount > 0:
                print("Instrutor removido com sucesso!")
                return True
            else:
                print("Instrutor não encontrado.")
                return False

        except Exception as e:
            print(f"Erro ao remover instrutor: {e}")
            if conexao:
                conexao.rollback()
            return False
        finally:
            if conexao:
                cursor.close()
                conexao.close()

    def get_instrutor_por_id(self, id_instrutor: int) -> Instrutor:
        """Busca um único instrutor pelo ID (útil para o Aluno)."""
        conexao = None
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()
            
            query = "SELECT id_instrutor, nome, especialidade FROM Instrutores WHERE id_instrutor = :1"
            cursor.execute(query, (id_instrutor,))
            
            resultado = cursor.fetchone()
            
            if resultado:
                return Instrutor(resultado[0], resultado[1], resultado[2])
            else:
                return None

        except Exception as e:
            print(f"Erro ao buscar instrutor por ID: {e}")
            return None
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
                
            # A query f-string é segura aqui pois validamos a 'tabela'
            # Convertendo para maiúsculas, pois Oracle é case-sensitive
            query = f"SELECT COUNT(1) FROM {tabela.upper()}"
            
            # O nome das tabelas no Oracle pode ser case-sensitive
            # Vamos garantir que estão maiúsculas no script SQL
            if tabela == 'alunos':
                query = "SELECT COUNT(1) FROM Alunos"
            elif tabela == 'instrutores':
                query = "SELECT COUNT(1) FROM Instrutores"
            
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