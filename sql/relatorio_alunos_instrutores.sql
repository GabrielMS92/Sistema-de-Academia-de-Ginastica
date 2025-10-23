-- Relatório 1: Lista Alunos e seus respectivos Instrutores (JOIN)
SELECT 
    a.nome AS Aluno, 
    a.email AS Email_Aluno, 
    COALESCE(i.nome, '*** SEM INSTRUTOR ***') AS Instrutor,
    COALESCE(i.especialidade, 'N/A') AS Especialidade_Instrutor
FROM 
    Alunos a
LEFT JOIN 
    Instrutores i ON a.id_instrutor_responsavel = i.id_instrutor
ORDER BY
    Instrutor, Aluno;