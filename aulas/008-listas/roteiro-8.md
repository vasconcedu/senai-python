# 💻 Roteiro 8

**⚠️ ATENÇÃO:** O desenvolvimento deste roteiro valerá como a Atividade em Sala AS-5. O professor avaliará o desempenho dos alunos **durante o desenvolvimento dos exercícios em sala de aula,** de forma a atribuir a nota avaliativa. Os arquivos de respostas **NÃO** serão recolhidos, mas somente analisados pelo professor em sala, para atribuição da nota.

## Exercício 1

Modifique o programa que você escreveu no roteiro 7 para utilizar uma lista de alunos carregada a partir de um arquivo chamado `alunos.txt`. Utilize o arquivo `alunos.txt` já existente no repositório como ponto de partida. 

O seu programa deve implementar as mesmas operações que o programa que você desenvolveu no roteiro 7, com a diferença de que, agora, a lista de alunos deve ser carregada a partir do arquivo, e não declarada estaticamente no programa como antes (ou seja, `alunos = []`).

No lugar disso, faça a leitura do arquivo para a lista `alunos` no início do programa. Execute as operações normalmente sobre a lista `alunos`, modificando somente a operação 6 (sair).

No lugar de somente encerrar a execução do programa, a operação 6, nessa nova versão do programa, deve salvar o conteúdo da lista no arquivo `alunos.txt`, de forma que, a cada execução do programa, o arquivo reflita as modificações que foram realizadas na lista, preservando o seu estado em disco para a sua próxima execução. 
