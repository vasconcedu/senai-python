# 💻 Roteiro 10

**⚠️ ATENÇÃO:** O desenvolvimento deste roteiro valerá como a Atividade em Sala AS-6. O professor avaliará o desempenho dos alunos **durante o desenvolvimento dos exercícios em sala de aula,** de forma a atribuir a nota avaliativa. Os arquivos de respostas **NÃO** serão recolhidos, mas somente analisados pelo professor em sala, para atribuição da nota.

## Exercício 1

Escreva uma função chamada `d` que recebe duas tuplas, representando as coordenadas de dois pontos no plano cartesiano, e que retorna a distância entre esses dois pontos.

Lembrete: a distância entre dois pontos `p1 = (x1, y1)` e `p2 = (x2, y2)` no plano cartesiano é dada por:

`d(p1, p2) = √( (x2 - x1)² + (y2 - y1)² )`

> **💡 Dica:** a função `math.sqrt`, do módulo `math`, calcula a raiz quadrada de um número.

## Exercício 2 

Escreva um programa que gera uma lista contendo 3 listas aninhadas, sendo que cada lista aninhada deve conter 3 números com ponto flutuante entre `0.0` e `10.0`, gerados pseudoaleatoriamente, isto é, utilizando o módulo `random`.

> **🎯 Exemplo:** o seu programa deve ser capaz de gerar algo parecido com: 
>
> `[[3.560213059267051, 5.50984129266038, 6.565433243793849], [7.878114678971176, 8.217532291303826, 8.80352873609867], [1.6377136433951778, 1.9478240823153647, 3.340258464069512]]`

> **💡 Dica:** a função `random.random` retorna um número pseudoaleatório entre `0.0` e `1.0`. Para gerar um número entre `0.0` e `10.0`, você deverá multiplicar o valor retornado pela função `random.random` por `10`.

## Exercício 3

Escreva um programa em Python que recebe como entradas os nomes e as notas de cada um dos alunos de uma turma.

O seu programa deve armazenar cada nome e nota lidos em uma lista aninhada, e as listas aninhadas, por sua vez, devem ser armazenadas em uma lista.

O seu programa deve ler nomes e notas até o usuário digitar a palavra `"parar"` ao ler o nome de um aluno. Quando isso acontecer, o seu programa deve mostrar a lista de alunos e notas na tela e, em seguida, encerrar a execução. 

> **💡 Atenção:** use uma função para ler os pares `nome, nota` de cada aluno. Faça a função retornar uma tupla após a leitura, contendo o nome e a nota de cada aluno. Ex.: `("Jose", 0.0)`.

## Exercício 4

A pasta `gastos/` contém uma implementação básica de um gerenciador de gastos pessoais utilizando o módulo `streamlit`, no arquivo `gastos.py`. Siga os passos abaixo para executar o programa `gastos.py`:

1. Vá até o terminal e execute o comando `pip install streamlit`;
2. Em seguida, navegue até a pasta `gastos/`;
3. Execute o comando `python -m streamlit run gastos.py`.

Depois, use o seu navegador web para ir até o endereço HTTP indicado no terminal. Familiarize-se com as funcionalidades da aplicação, respondendo: 

4. Descreva, com suas palavras, o que a aplicação faz.
5. Na função "Cadastrar", quantos e quais são os parâmetros utilizados para cadastrar um novo gasto?
6. Quanto custou a pizza no dia 09/05/2025?
7. Gere um relatório de gastos entre os dias 01/01/2025 e 30/06/2025 e mostre ao professor.
8. Qual foi a categoria com a qual o usuário mais gastou no período considerado no relatório acima?

Em seguida, familiarize-se com o código da aplicação. Abra o arquivo `gastos.py` no VS Code e responda:

9. Quantas funções o código tem? 
10. De onde vêm os nomes das categorias de gastos que o programa é capaz de cadastrar?
11. Onde o programa armazena os gastos cadastrados?
12. Quais são os tipos de estruturas de dados do Python que são utilizados para armazenar os gastos cadastrados?
13. Qual é o nome da função que efetua o cadastro de um novo gasto? 

Por último, implemente a funcionalidade de cadastrar observações sobre os gastos: 

14. Modifique a estrutura de dados já existente em disco para levar em consideração a criação de um novo campo chamado `"observacoes"`. Esse novo campo deve ter o valor vazio, ou seja, `""`,  para todos os cadastros **já existentes** na estrutura de dados. Depois de modificar a estrutura de dados, mostre as suas modificações ao professor antes de prosseguir;
15. Modifique a função que efetua o cadastro de um novo gasto para adicionar um novo parâmetro a ser cadastrado, chamado "Observações". Esse novo parâmetro deve ser do tipo texto, assim como é o parâmetro de cadastro "Nome", e deve possibilitar ao usuário cadastrar observações a respeito do gasto cadastrado, preenchendo o campo `"observacoes"` que você adicionou à estrutura de dados.
