# 💻 Roteiro 7

**⚠️ ATENÇÃO:** O desenvolvimento deste roteiro valerá como a Atividade em Sala AS-5. O professor avaliará o desempenho dos alunos **durante o desenvolvimento dos exercícios em sala de aula,** de forma a atribuir a nota avaliativa. Os arquivos de respostas **NÃO** serão recolhidos, mas somente analisados pelo professor em sala, para atribuição da nota.

## Exercício 1

O arquivo `exercicio-1.py` contém uma lista com 1000 nomes de alunos.

Modifique o arquivo para adicionar um laço `for` que mostra na tela os nomes de todos os alunos contidos na lista.

## Exercício 2 

O arquivo `exercicio-2.py` contém a base de um programa de cadastro de alunos.

Modifique o programa para implementar as operações de cadastro, utilizando as operações básicas de listas:

1. Se o usuário selecionar a operação 1, o programa deve pedir que o usuario digite o nome de um novo aluno a ser adicionado à lista de cadastro e, em seguida, adicionar o novo aluno à lista;
2. Se o usuário selecionar a operação 2, o programa deve pedir o índice de um aluno e, em seguida, mostrar o nome do aluno cujo índice na lista de cadastro corresponde ao índice fornecido pelo usuário;
    
    > 🚨 ATENÇÃO: se o índice fornecido pelo usuário for inválido, o programa deve mostrar essa informação na tela!

3. Se o usuário selecionar a operação 3, o programa deve pedir o nome de um aluno e, em seguida, remover esse aluno da lista de cadastro;

    > 🚨 ATENÇÃO: se o nome fornecido pelo usuário não existir na lista de cadastro, o programa deve mostrar essa informação na tela!

    > 💡 Dica: você pode usar `range(0, len(alunos))` em um laço `for` para iterar sobre a lista com base nos índices dos alunos.

4. Se o usuário selecionar a operação 4, o programa deve mostrar a lista completa de alunos cadastrados;
5. Se o usuário selecionar a operação 5, o programa deve apagar todos os alunos da lista.
