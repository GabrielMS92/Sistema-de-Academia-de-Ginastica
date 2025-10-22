erDiagram
    ALUNO {
        NUMBER id_aluno PK "Identificador do Aluno"
        VARCHAR nome "Nome Completo"
        VARCHAR cpf "CPF (Único)"
        VARCHAR telefone
        DATE data_nascimento
        VARCHAR email "Email (Único)"
    }

    INSTRUTOR {
        NUMBER id_instrutor PK "Identificador do Instrutor"
        VARCHAR nome "Nome Completo"
        VARCHAR especialidade "Área de Atuação"
        VARCHAR telefone
    }

    PLANO {
        NUMBER id_plano PK "Identificador do Plano"
        VARCHAR nome_plano "Nome do Plano"
        NUMBER valor "Preço do Plano"
        NUMBER duracao_meses "Duração em Meses"
        NUMBER id_instrutor FK "Instrutor Responsável (Opcional)"
    }

    MATRICULA {
        NUMBER id_aluno PK,FK "Referência ao Aluno (Chave Composta)"
        NUMBER id_plano PK,FK "Referência ao Plano (Chave Composta)"
        DATE data_matricula PK "Data da Matrícula (Chave Composta)"
        CHAR ativo "Status (S/N)"
    }

    FREQUENCIA {
        NUMBER id_frequencia PK "Identificador do Registro"
        NUMBER id_aluno FK "Referência ao Aluno"
        NUMBER id_instrutor FK "Referência ao Instrutor"
        DATE data_aula "Data e Hora da Aula"
        CHAR presenca "Presença (P/F)"
    }

    %% Relacionamento (Cardinalidade)
    ALUNO ||--o{ MATRICULA : "se matricula em"
    PLANO ||--o{ MATRICULA : "registra o plano"
    INSTRUTOR ||--o{ PLANO : "é responsável por"
    ALUNO ||--o{ FREQUENCIA : "registra a"
    INSTRUTOR ||--o{ FREQUENCIA : "acompanha na"
