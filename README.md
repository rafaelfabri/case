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

Vamos começar com os items de maior Lift, que está representado na imagem abaixo 

![exemplo 2](https://github.com/rafaelfabri/case/blob/main/imagens/exemplo_support.png)



# Parte 2: Data Science

# Parte 3: Pipeline de dados
