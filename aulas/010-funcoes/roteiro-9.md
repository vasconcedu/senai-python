# 💻 Roteiro 8

**⚠️ ATENÇÃO:** O desenvolvimento deste roteiro valerá como a Atividade em Sala AS-6. O professor avaliará o desempenho dos alunos **durante o desenvolvimento dos exercícios em sala de aula,** de forma a atribuir a nota avaliativa. Os arquivos de respostas **NÃO** serão recolhidos, mas somente analisados pelo professor em sala, para atribuição da nota.

## Exercício 1

Escreva um programa que recebe como entradas dois números decimais e uma operação aritmética (`+`, `-`, `*` ou `/`).

Em seguida, o programa deve calcular o resultado da operação aritmética lida e mostrar o resultado na tela.

Você deve implementar cada operação aritmética como uma função diferente:

- A função `soma(a, b)` retorna a soma de a com b;
- A função `subtracao(a, b)` retorna a subtração de b de a;
- A função `multiplicacao(a, b)` retorna a multiplicação de a por b; e
- A função `divisao(a, b)` retorna a divisão de a por b.

## Exercício 2

Escreva um programa que implementa as seguintes funções:

- `conta_caracteres(s)`: retorna o número de caracteres da string s;
- `conta_linhas(s)`: retorna o número de linhas da string s.

Em seguida, faça o seu programa ler o arquivo `cancao-do-exilio.txt` e mostrar na tela:

- O número de caracteres do poema;
- O número de linhas do poema.

## Exercício 3

Escreva uma função que verifica se uma string é um palíndromo, ou seja, se a string lida normalmente é igual à string lida ao contrário. Exemplos:

- A string `arara` é um palíndromo, porque `arara` ao contrário é `arara`;
- A string `araraquara` não é um palíndromo, porque `araraquara` ao contrário é `arauqarara`.

A sua função deve retornar `True` se a string for um palíndromo, e `False` se a string não for um palíndromo.

Em seguida, escreva um programa que recebe uma string do usuário e, usando a função que você escreveu, diga ao usuário se a string fornecida é um palíndromo ou não. 

## Exercício 4 (desafio)

Escreva uma função chamada `fib(n)`, que calcula a sequência de Fibonacci até a n-ésima posição. 

Por exemplo, se a função receber o número 8, ela deve calcular a sequência de Fibonacci até a 8ª posição, isto é:

```
Posição:                0 1 2 3 4 5 6 7
Sequência de Fibonacci: 0 1 1 2 3 5 8 13
```

Em seguida, utilize a sua função para escrever um programa que recebe um número n do usuário e calcula a sequência de Fibonacci até a n-ésima posição.

Obs.: como calcular a sequência de Fibonacci? 

Sendo Fib(i) o i-ésimo número da sequência de Fibonacci: 

- Fib(i) = Fib(i-1) + Fib(i-2); sendo que:

- Fib(1) = 1; e
- Fib(0) = 0.

> 💡 Dica: comece pensando nos casos mais simples: você sabe que Fib(0) = 0. Logo, o que a sua função deve retornar se n for 0? Você também sabe que Fib(1) = 1. Logo, o que a sua função deve retornar se n for 1? Por último, pense no caso mais complexo: como calcular os números da sequência de Fibonacci a partir da 3ª posição, isto é, quando n >= 2? 
