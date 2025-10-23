import os
from conexion import criar_conexao
from prettytable import PrettyTable # Biblioteca para interface amigável

class Relatorios:
    
    def __init__(self):
        # Define o caminho base para a pasta SQL
        self.base_path = os.path.join(os.path.dirname(__file__), '..', 'sql')

    def _ler_query_sql(self, nome_arquivo: str) -> str:
        """Lê o conteúdo de um arquivo .sql."""
        caminho_arquivo = os.path.join(self.base_path, nome_arquivo)
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Erro: Arquivo de relatório não encontrado em {caminho_arquivo}")
            return None
        except Exception as e:
            print(f"Erro ao ler arquivo SQL: {e}")
            return None

    def executar_relatorio(self, nome_arquivo: str):
        """Executa uma query lida do arquivo e exibe em uma tabela."""
        query_bruta = self._ler_query_sql(nome_arquivo)
        if not query_bruta:
            return
            
        # --- [A CORREÇÃO ESTÁ AQUI] ---
        # Limpa espaços em branco no início/fim e remove qualquer ';' no final.
        query_limpa = query_bruta.strip().rstrip(';')
        # --- [FIM DA CORREÇÃO] ---

        conexao = None
        try:
            conexao = criar_conexao()
            if conexao is None:
                print("Não foi possível conectar ao banco de dados para gerar o relatório.")
                return
                
            cursor = conexao.cursor()
            
            # Executa a query limpa, em vez da bruta
            cursor.execute(query_limpa)
            
            # Pega os nomes das colunas
            nomes_colunas = [desc[0] for desc in cursor.description]
            
            # Pega os resultados
            resultados = cursor.fetchall()

            # Exibe usando PrettyTable para uma "interface amigável"
            tabela = PrettyTable()
            tabela.field_names = nomes_colunas
            
            if not resultados:
                # Adiciona uma linha "vazia" formatada se não houver resultados
                tabela.add_row(["-" * col_len for col_len in range(len(nomes_colunas))])
            else:
                for linha in resultados:
                    tabela.add_row(linha)
            
            print(f"\n--- RESULTADO: {nome_arquivo} ---")
            print(tabela)

        except Exception as e:
            print(f"Erro ao executar relatório: {e}")
            # Adiciona um help extra para o ORA-00933
            if "ORA-00933" in str(e):
                print("Dica: Verifique se o arquivo .sql não contém um ';' no final.")
        finally:
            if conexao:
                cursor.close()
                conexao.close()
