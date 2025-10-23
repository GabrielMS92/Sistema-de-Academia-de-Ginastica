import os
from conexion import criar_conexao

SCRIPT_FILE = 'script_bd.sql'

def run_setup():
    print(f"--- INICIANDO SETUP DO BANCO DE DADOS ORACLE ---")
    print(f"Tentando executar o script: {SCRIPT_FILE}...")
    
    conexao = None
    try:
        # 1. Conectar ao banco
        conexao = criar_conexao()
        if conexao is None:
            print("ERRO: Falha ao conectar. Verifique 'conexion.py' e se o Oracle está no ar.")
            return

        print("Conexão bem-sucedida.")

        # 2. Ler o conteúdo do arquivo SQL
        print("Lendo script 'script_bd.sql'...")
        with open(SCRIPT_FILE, 'r', encoding='utf-8') as f:
            script_completo = f.read()

        # 3. O script do Oracle usa '/' como separador de comandos
        # Vamos dividir o script por esse separador
        comandos = script_completo.split('/')
        
        cursor = conexao.cursor()
        
        print(f"Encontrados {len(comandos)} comandos. Executando...")
        
        comando_num = 1
        for comando in comandos:
            comando_limpo = comando.strip() # Limpa espaços em branco e novas linhas
            
            # Ignora comandos vazios (resultantes de '//' ou do final do arquivo)
            if comando_limpo: 
                print(f"  Executando comando {comando_num}...")
                try:
                    cursor.execute(comando_limpo)
                    print(f"  -> Comando {comando_num} OK.")
                except Exception as e:
                    # Ignora o erro "table or view does not exist" que acontece nos DROPs
                    if "ORA-00942" in str(e):
                        print(f"  -> Info: Tabela não existia (Ignorando ORA-00942).")
                    else:
                        # Se for outro erro, mostra e para
                        print(f"ERRO AO EXECUTAR COMANDO {comando_num}: {e}")
                        raise e # Levanta o erro para parar o script
            
            comando_num += 1

        print("\n--- SCRIPT EXECUTADO COM SUCESSO! ---")
        
        # O script_bd.sql já tem um COMMIT, mas o driver oracledb
        # pode precisar de um commit explícito após a execução.
        conexao.commit()
        print("Banco de dados salvo (COMMIT executado).")

    except Exception as e:
        print(f"\n--- ERRO CATASTRÓFICO DURANTE O SETUP ---")
        print(f"Erro: {e}")
        if conexao:
            print("Revertendo transações (ROLLBACK)...")
            conexao.rollback()
    finally:
        if conexao:
            cursor.close()
            conexao.close()
            print("Conexão fechada.")

# --- Ponto de Entrada ---
if __name__ == "__main__":
    run_setup()