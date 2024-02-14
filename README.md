# Parte 1: Analytics

A análise feita na parte 1 encontra-se em um jupyter notebook neste repositório do GitHub:
case/notebooks/parte_1_analytics.ipynb
https://github.com/rafaelfabri/case/blob/main/notebooks/parte_1_analytics.ipynb

## Market Basket Analysis

A market Basket analysis tem como ideia trazer número de associacões entre produtos. Utilizando estatistíca com teoria de interseçao, união, etc. Para esse case foi calculado 3 métricas utilizando o apriori algoritimo para responder as perguntar da parte 1:

* Support: Frequencia que o item A apareceu nas cestas (produtos com maior support foram os mais relevantes no período);

\begin{equation}
    Support(P(A)) = \frac{P(A)}{n}  
\end{equation}

* Confidence: Escolhendo um item X como support (item com maior frequancia), das vezes que o item X esta na cesta qual é a chance do item Y também estar;
* Lift: A quantidade de vezes que se o item Y vai ser escolhido se item X for comprado.


Utilizando a métrica support para descobrir os items mais relevantes neste período do estudo, foi encontrado os 10 items abaixo com maior support:

![exemplo 1](https://github.com/rafaelfabri/case/blob/main/imagens/support_antecede.png)

![exemplo 2](https://github.com/rafaelfabri/case/blob/main/imagens/exemplo_support.png)



# Parte 2: Data Science

# Parte 3: Pipeline de dados
