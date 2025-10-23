-- Relatório 2: Contagem de alunos por instrutor (GROUP BY)
SELECT 
    i.nome AS Instrutor,
    COUNT(a.id_aluno) AS "Quantidade de Alunos"
FROM 
    Instrutores i
LEFT JOIN 
    Alunos a ON i.id_instrutor = a.id_instrutor_responsavel
GROUP BY
    i.id_instrutor, i.nome
ORDER BY
    "Quantidade de Alunos" DESC;