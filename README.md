# Parte 1: Analytics

A análise feita na parte 1 encontra-se em um jupyter notebook neste repositório do GitHub:
case/notebooks/parte_1_analytics.ipynb
https://github.com/rafaelfabri/case/blob/main/notebooks/parte_1_analytics.ipynb

## Market Basket Analysis

![Fluxograma](https://github.com/rafaelfabri/case/blob/main/imagens/img1.jpg)

A market Basket analysis tem como ideia trazer número de associacões entre produtos. Utilizando estatistíca com teoria de probabilidade, interseçao, união, etc. Para a parte 1 deste case foi calculado 3 métricas Support (Apoio), Confidence (Confiança), Lift (Levantamento):

* Support: é a frequencia que o produto A apareceu nas cestas/ticket dividido pelo número total de transações, em resumo é o percentual que o produto A apareceu nas cestas daquele determinado período;

$$Support(P(A)) = \frac{qtd A}{n}$$


	* qtd A Frequência que o item A apareceu nas cestas em um respectivo período;
	* n Quantidade total de cestas naquele respectivo período.


* Confidence: Qual é a probabilidade do item B ser comprado dado que o item A também seja comprado;


$$Confidence(P(B | A)) = \frac{P(A U B)}{Support(P(A))}$$


	* (P(B | A)) Probabilidade de B ser escolhido se A for escolhido;
	* P(A U B) Interseção entre A e B, percentual de cestas que A e B foram comprados juntos.
		* P(A U B) = \frac{P(A \cap B)}{n}
		
* Lift: A chance do item B ser comparado se item A também for, levando em consideração toda a popularidade de B. As duas equações abaixo podem ser aplicadas para calcular o Lift.


$$Lift = \frac{Confidence(P(B | A))}{Support(P(B)}$$




$$Lift= \frac{P(A U B)}{Support(P(A))*Support(P(B))}$$




Utilizando essas métricas vamos conseguir verificar os 10 items mais relevantes no período do conjunto de dados, também verificar os 15 items que acompanham esses cada um dos respectivos items e encontrar oportunidades de combos/promoções em conjunto.

Com essas métricas vamos conseguir responder as perguntas feitas na Parte 1 deste estudo de caso. O fluxograma abaixo mostra a lógica simplificada do que foi feito no código para chegar na tabela final com os valores.

![img1](https://github.com/rafaelfabri/case/blob/main/imagens/fluxograma_mba.png)

Os 10 items mais relevantes de acordo com a métrica support encontra-se abaixo no gráfico e na tabela: 


![support antecede grafico](https://github.com/rafaelfabri/case/blob/main/imagens/10_items_mais_relevantes.png)


![support antecede](https://github.com/rafaelfabri/case/blob/main/imagens/support_antecede.png)

A SACOLA PLASTICA MM BRANCA é o produto teve maior percentual de saídas no respectivo período da base de dados, das 874.860 cestas 3,3% foram SACOLA PLASTICA MM BRANCA. Porteriormente vem SACOLA PLASTICA MM CINZA, PAPEL TOALHA.., etc.

Agora que sabemos que esses são os 10 items mais relevantes, vamos ver os produtos mais significativos que o acompanham nas cestas, para ver isso vamos vamos ver os 15 produtos com maior quantidade referente a cada um dos items A calcular a confidence P(B|A), support(B) e Lift.

A métrica principal aqui será o Lift, mas para entendermos ela será necessário utilizarmos a confidence e support(B).

Vamos começar com os items de maior Lift, que está representado na Tabela abaixo:

![exemplo 2](https://github.com/rafaelfabri/case/blob/main/imagens/tabela_final_parte_1.png)

Dentre os 10 items mais relevantes, o item LEITE CONDENSADO TP 395G PIRACANJ (B) possui o maior Lift (37.84) quando item CR DE LEITE PIRACANJUBA TP 200G (A) está na cesta.

Isso significa que quando é colocado na cesta um CR DE LEITE PIRACANJUBA TP 200G a chance desse cliente também comprar LEITE CONDENSADO TP 395G PIRACANJ aumenta em 37 vezes. A explicação desse valor vem da relaçao da confidence com o support_consequencia que é referente ao item B. Portanto, quando observamos, existe aproximadamente 4,5% de probabilidade do item B ser adquirido dado que o item A também foi adquirido, é uma probabilidade pequena, mas quando comparamos isoladamente a propabilidade do item B ser comprado é de 0,11% (support_consequencia), assim quando adiquirido o item A a chance do item B também se adquirido é 37 vezes maior.

Aqui podemos ver uma oportunidade de alavancar a venda do LEITE CONDENSADO que é comprado apenas 0,11% das vezes:
* se colocarmos leite condesado próximo ao leite;
* montar promomoções na compra de duas caixa de leite o cliente ganha um desconto no leite condensado;
* montar Kit de vendas.

Para entendermos um pouco de como a métrica Lift se comparta podemos ver a matriz abaixo:

![Matriz](https://github.com/rafaelfabri/case/blob/main/imagens/matriz.png)

* **Lift <= 1** isso mostra que não temos evidencias suficientes que o cliente que fazer aquisição do item A também vai fazer a aquisição so item B.
* **Lift > 1** isso mostra indicios que a aquisição do item A aumenta a chance da aquisição do item B

Para chegarmos nesses resultados do Lift tem 4 possibilidades:
1) Confidence Alto e Support Alto: Quando se tem a condidence(P(B|A)) alto isso indica que existe uma grande probabilidade do item B ser adiquirido quando o item A também for. No entanto, o item B isoladamente já possui uma alta probabilidade de aquisição. Portanto, não há um questão de associação entre o item A e o item B, mas sim uma semelhança por os dois item serem items que saem bastante.
2) Confidence Alto e Support Pequeno: Esse caso representa o exemplo acima, a confidence é alta fazendo o item B ter uma alta probabilidade de ser adquirido se o item A também for adquirido. Quando olhamos isoladamente o item B os clietes fazer pouca aquisição dele, mas quando acompanhado do item A a chance dele ser comprado aumenta.
3) Confidence Pequeno e Support Alto: A confidence dos dois produtos é pequena, mas o support do item B é alto, o que provoca um Lift menor que 1, o item A e B são comprados individualmente não sendo associados.
4) Confidence Pequeno e Support Pequeno: Nesse caso os dois são pequenos, não há indicios suficientes para dizermos que os items são associados.


![exemplo 3](https://github.com/rafaelfabri/case/blob/main/imagens/tabela_final_parte_1_.png)



# Parte 2: Data Science

![img 1](https://github.com/rafaelfabri/case/blob/main/imagens/Algoritmo_Apriori.png)

# Parte 3: Pipeline de dados
