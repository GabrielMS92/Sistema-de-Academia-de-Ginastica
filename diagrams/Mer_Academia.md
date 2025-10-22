classDiagram
    direction TB
    
    class INSTRUTOR {
        +Integer id_instrutor (PK)
        +String nome (Obrigatório)
        +String telefone
        +String especialidade
    }
    
    class ALUNO {
        +Integer id_aluno (PK)
        +String nome (Obrigatório)
        +String cpf (Obrigatório)
        +Date data_nascimento
        +Integer id_instrutor (FK)
    }
    
    INSTRUTOR "1" -- "N" ALUNO : treina
