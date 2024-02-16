# Parte 1: Analytics

A análise feita na parte 1 encontra-se em um jupyter notebook neste repositório do GitHub:
case/notebooks/parte_1_analytics.ipynb
https://github.com/rafaelfabri/case/blob/main/notebooks/parte_1_analytics.ipynb

## Market Basket Analysis

![img1](https://github.com/rafaelfabri/case/blob/main/imagens/fluxograma_mba.png)

A market Basket analysis tem como ideia trazer número de associacões entre produtos. Utilizando estatistíca com teoria de probabilidade, interseçao, união, etc. Para a parte 1 deste case foi calculado 3 métricas Support (Apoio), Confidence (Confiança), Lift (Levantamento):

* Support: é a frequencia que o produto A apareceu nas cestas/ticket dividido pelo número total de transações, em resumo é o percentual que o produto A apareceu nas cestas daquele determinado período;

```math

    Support(P(A)) = \frac{qtd A}{n}
    
```

	* qtd A Frequência que o item A apareceu nas cestas em um respectivo período;
	* n Quantidade total de cestas naquele respectivo período.


* Confidence: Qual é a probabilidade do item B ser comprado dado que o item A também seja comprado;

```math

    Confidence(P(B | A)) = \frac{P(A U B)}{Support(P(A))}

```

	* (P(B | A)) Probabilidade de B ser escolhido se A for escolhido;
	* P(A U B) Interseção entre A e B, percentual de cestas que A e B foram comprados juntos.
		* P(A U B) = \frac{P(A \cap B)}{n}
		
* Lift: A chance do item B ser comparado se item A também for, levando em consideração toda a popularidade de B. As duas equações abaixo podem ser aplicadas para calcular o Lift.

```math

    Lift = \frac{Confidence(P(B | A))}{Support(P(B)} 

```

```math
    Lift= \frac{P(A U B)}{Support(P(A))*Support(P(B))} 
```

Com essas métricas vamos conseguir responder as perguntas feitas na Parte 1 deste estudo de caso. A imagem abaixo explica um pouco como.


Utilizando essas métricas vamos conseguir verificar os 10 items mais relevantes no período do conjunto de dados, também verificar os 15 items que acompanham esses cada um dos respectivos items e encontrar oportunidades de combos/promoções em conjunto.

![Fluxograma](https://github.com/rafaelfabri/case/blob/main/imagens/img1.jpg)

Abaixo encontra-se os 10 items mais relevantes que possuem maior support:

![exemplo 1](https://github.com/rafaelfabri/case/blob/main/imagens/support_antecede.png)

![exemplo 2](https://github.com/rafaelfabri/case/blob/main/imagens/exemplo_support.png)



# Parte 2: Data Science

# Parte 3: Pipeline de dados
