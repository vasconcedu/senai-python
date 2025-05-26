# 💻 Roteiro 3

## Exercício 1

Escreva um programa chamado `senha.py`, que recebe uma string como entrada e que mostra como saídas:

* A mensagem "Voce acertou a senha", se a entrada recebida for "senhasupersegura"; ou
* "Voce errou a senha", se a entrada recebida for qualquer outra coisa diferente da string "senhasupersegura".

## Exercício 2

Escreva um programa que recebe um número inteiro como entrada e, em seguida, mostra na tela "Par", se o número for par, ou "Impar", se o número for ímpar.

## Exercício 3

Em uma galáxia muito, muito distante, existem 3 planetas, habitados por 3 povos diferentes:

* O povo Glib, que habita o planeta Glibbia;
* O povo Warg, que habita o planeta Warggia; e
* O povo Mik, que habita o planeta Mikkia.

Escreva um programa que recebe como entrada o nome de um povo e que mostra como saída o nome do planeta onde aquele povo habita. Por exemplo: se o programa receber como entrada "Glib", ele deve mostrar como saída: 

> O povo Glib habita o planeta Glibbia.

## Exercício 4 (contém desafio)

A família Bolseirinho tinha 5 filhos: 

* Pimpilio, que era o primogênito;
* Florisbela, que era a segunda filha;
* Zezeco, que era o terceiro filho;
* Nhonhoaldo, que era o quarto filho; e 
* Gliceria, que era a caçula.

Escreva um programa que recebe um número inteiro e que mostra, como saída, o nome do filho correspondente ao número recebido. Por exemplo, se o programa receber o número 3, ele deve mostrar como saída: 

> O terceiro filho da família Bolseirinho é o Zezeco.

**Desafio:** se um número maior do que o número de filhos da família Bolseirinho for recebido como entrada, o programa deve mostrar como saída: 

> O número digitado é maior do que o número de filhos da família Bolseirinho!

## 🔥 Exercício 5 (super desafio)

**Obs.: não é necessário resolver este exercício, pois ele contempla conceitos que nós ainda vamos estudar. No entanto, alunos que já têm experiência prévia na área de programação e/ou que tenham concluído os exercícios 1-4 com muita antecedência podem tentar resolvê-lo.**

1. Desenhe um fluxograma que represente o funcionamento do cofre digital do Gandalf, que funciona da seguinte forma: 

    * O usuário tem 3 tentativas para acertar uma senha;
    * Inicialmente, o cofre exibe a mensagem "Fale, amigo, e entre. Qual eh a senha correta? 3 tentativas restantes ate a autodestruicao...";
    * A senha correta é a string "Um anel para a todos governar";
    * Após cada tentativa incorreta, o cofre diminui o número de tentativas restantes e exibe a mensagem "A senha foi esquecida ate mesmo pelos sabios de Valfenda. Voce possui X tentativas restantes...", onde X é o número de tentativas restantes; 
    * Se o usuário acertar a senha, o cofre exibe "O caminho esta livre..." e abre;
    * Se o usuário errar 3 vezes, o cofre exibe "Voce nao passara!" e se autodestrói nas chamas de Mordor.

2. Em seguida, implemente um programa em Python que simula o comportamento do cofre digital do Gandalf, com base no fluxograma que você desenhou.
