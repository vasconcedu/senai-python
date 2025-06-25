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

> **💡 Dica:** a função `random.random` retorna um número pseudoaleatório entre `0.0` e `1.0`. Para gerar um número entre `0.0` e `10.0`, você deverá multiplicar o valor retornado pela função `random.random` por `10.0`.
