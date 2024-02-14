# Parte 1: Analytics

A análise feita na parte 1 encontra-se em um jupyter notebook neste repositório do GitHub:
case/notebooks/parte_1_analytics.ipynb
https://github.com/rafaelfabri/case/blob/main/notebooks/parte_1_analytics.ipynb

## Market Basket Analysis

A market Basket analysis tem como ideia trazer número de associacões entre produtos. Utilizando estatistíca com teoria de interseçao, união, etc. Para esse case foi calculado 3 métricas utilizando o apriori algoritimo para responder as perguntar da parte 1:

* Support: Frequencia que o item A apareceu nas cestas (produtos com maior support foram os mais relevantes no período);


   $$ Support(P(A)) = \frac{P(A)}{n} $$ 
   
	* P(A) Frequência que o item A apareceu nas cestas em um determinado período;
	* n Quantidade total de cestas naquele período.


* Confidence: Escolhendo um item A como support (item com maior frequancia), das vezes que o item A esta na cesta qual é a chance do item B também estar;


   $$ Confidence(P(B | A)) = \frac{P(A \cap B)}{Support(P(A))} $$ 

	* (P(B | A)) Probabilidade de B ser escolhido se A for escolhido;
	* P(A \cap B) Interseção entre A e B, quantidade de cestas que A e B estão juntos.

* Lift: A quantidade de vezes que se o item Y vai ser escolhido se item X for comprado.


   $$ Confidence(P(B | A)) = \frac{Confidence(P(B | A))}{Support(P(B)} $$ 

Utilizando essas métricas vamos conseguir verificar os 10 items mais relevantes no período do conjunto de dados e também verificar os 15 items que acompanham esses cada um dos respectivos items.

Abaixo encontra-se os 10 items mais relevantes que possuem maior support:

![exemplo 1](https://github.com/rafaelfabri/case/blob/main/imagens/support_antecede.png)

![exemplo 2](https://github.com/rafaelfabri/case/blob/main/imagens/exemplo_support.png)



# Parte 2: Data Science

# Parte 3: Pipeline de dados
