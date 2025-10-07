erDiagram
    ALUNO {
        NUMBER id_aluno PK
        VARCHAR nome
        VARCHAR cpf
        VARCHAR telefone
        DATE data_nascimento
        VARCHAR email
    }

    INSTRUTOR {
        NUMBER id_instrutor PK
        VARCHAR nome
        VARCHAR especialidade
        VARCHAR telefone
    }

    PLANO {
        NUMBER id_plano PK
        VARCHAR nome_plano
        NUMBER valor
        NUMBER duracao_meses
        NUMBER id_instrutor FK
    }

    MATRICULA {
        NUMBER id_matricula PK
        NUMBER id_aluno FK
        NUMBER id_plano FK
        DATE data_matricula
        CHAR ativo
    }

    FREQUENCIA {
        NUMBER id_frequencia PK
        NUMBER id_aluno FK
        NUMBER id_instrutor FK
        DATE data_aula
        CHAR presenca
    }

    %% RELACIONAMENTOS
    ALUNO ||--o{ MATRICULA : "possui"
    PLANO ||--o{ MATRICULA : "é associado"
    INSTRUTOR ||--o{ PLANO : "cria/oferece"
    ALUNO ||--o{ FREQUENCIA : "registra presença"
    INSTRUTOR ||--o{ FREQUENCIA : "acompanha"
