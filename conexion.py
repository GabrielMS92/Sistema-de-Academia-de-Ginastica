import oracledb
import os

# Configura o modo "Thick" (se o Instant Client estiver instalado) ou "Thin" (padrão)
# Vamos tentar o modo Thin primeiro, que não precisa de instalação extra
# oracledb.init_oracle_client() 

# --- Credenciais do arquivo image_feccb8.png ---
DB_HOST = "localhost"
DB_PORT = "1521"
DB_SERVICE_NAME = "XEPDB1"
DB_USER = "system"
DB_PASS = "oracle"

# Constrói o DSN (Data Source Name)
# Formato: "host:port/service_name"
DB_DSN = f"{DB_HOST}:{DB_PORT}/{DB_SERVICE_NAME}"

def criar_conexao():
    """Cria e retorna um objeto de conexão com o banco de dados Oracle."""
    conexao = None
    try:
        # Tenta conectar usando o modo "Thin" (padrão)
        conexao = oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)
        # print("Conexão com o Oracle bem-sucedida!") # Opcional
    except oracledb.Error as e:
        print(f"Erro ao conectar ao Oracle: '{e}'")
        print("Verifique se o Oracle XE está rodando, se o Listener está no ar e se as credenciais em 'conexion.py' estão corretas.")
    return conexao