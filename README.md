# Parte 1: Analytics

A análise feita na parte 1 encontra-se em um jupyter notebook neste repositório do GitHub:
case/notebooks/parte_1_analytics.ipynb
https://github.com/rafaelfabri/case/blob/main/notebooks/parte_1_analytics.ipynb

## Market Basket Analysis

![Fluxograma](https://github.com/rafaelfabri/case/blob/main/imagens/img1.jpg)

A Market Basket Analysis tem como objetivo trazer métricas de associacões entre produtos/items, essa associação é utilizada muito para setores de loja de varejo, mercados, lojas de convenência, etc. Utilizando conceitos básicos de estatistíca como teoria de probabilidade, interseçao, união, etc, pode-se chegar em valores que trazem insights interessante sobre a aquisição de produtos em cada cesta de compra. 

Portanto, nessa parte 1 deste estudo de caso vamos calcular 3 métricas pela metodologia Market Basket Analysis para entender a associação de produtos e responder as perguntas feitas. A métricas são Support (Apoio), Confidence (Confiança), Lift (Levantamento):

* Support: é a frequencia que o item A apareceu nas cestas/ticket dividido pelo número total de transações, em resumo é o percentual que o produto A apareceu nas cestas daquele determinado período;

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




Utilizando a métrica Support(P(A)) vamos conseguir verificar os 10 items mais relevantes no período do conjunto de dados e com as métricas de Confidence(P(B|A)) e Lift podemos entender os 15 items B que mais acompanham cada um dos respectivos items A. Desta forma, podemos entender melhor a associação de produtos na cesta dos consumidores e também sugerir combos/promoções para alavancar a venda.

> **Fluxograma**

O fluxograma abaixo mostra a lógica simplificada do que foi feito no código em Python que encontra-se no Jupyter notebook para consolidarmos a tabela final com os valores de cada métrica.

![img1](https://github.com/rafaelfabri/case/blob/main/imagens/fluxograma_mba.png)

> **10 items mais relevantes no período**


![support antecede grafico](https://github.com/rafaelfabri/case/blob/main/imagens/10_items_mais_relevantes.png)


![support antecede](https://github.com/rafaelfabri/case/blob/main/imagens/support_antecede.png)

Com a métrica Support(P(A)) conseguimos ver quais produtos tiverem maior aquísicao percentual no período. Observa-se, que a *SACOLA PLASTICA MM BRANCA* é o produto teve maior percentual de saídas, das 874.860 cestas 3,3% foram SACOLA PLASTICA MM BRANCA. Porteriormente vem *SACOLA PLASTICA MM CINZA*, *PAPEL TOALHA KITCHEN JUMB FD C360FL*, e assim por diante.

A partir destes 10 items A mais relevantes, pode-se verificar os items B que mais acompanham o item A nas cestas. Primeiramente, deve-se filtrar apenas as cestas com os items A e contar os items B que acompanham a cesta, deixando apenas os 15 produtos com maior frequência, a partir disso pode-se calcular a confidence P(B|A), support(B) e Lift.

A métrica principal aqui será o Lift, mas para entendermos ela será necessário utilizarmos a confidence e support(B).

Vamos começar com os items de maior Lift, que está representado na Tabela abaixo:

Antecede: item A
Consequência: item B

> **Resultados Consolidados**

![exemplo 2](https://github.com/rafaelfabri/case/blob/main/imagens/tabela_final_parte_1.png)

:chart_with_upwards_trend: Dentre os 10 items mais relevantes, o item *LEITE CONDENSADO TP 395G PIRACANJ* (B) possui o maior Lift (37.84) quando item *CR DE LEITE PIRACANJUBA TP 200G* (A) está na cesta.

:bulb: Isso significa que quando é colocado na cesta um *CR DE LEITE PIRACANJUBA TP 200G* a chance desse cliente também comprar *LEITE CONDENSADO TP 395G PIRACANJ* aumenta em 37 vezes. 

A explicação desse valor ocorre da relaçao da confidence com o support_consequencia. 

:bulb: Quando observamos, existe aproximadamente 4,5% de probabilidade do item B ser adquirido dado que o item A também foi adquirido, é uma probabilidade pequena, mas quando comparamos isoladamente a propabilidade do item B ser comprado é de 0,11% (support_consequencia) sendo um item esteve em poucas cestas neste período. Portanto, quando o item A está em na cesta de um determinado cliente a chance do item B também ser adicionada é 37 vezes maior.

:chart_with_upwards_trend: Aqui podemos ver uma oportunidade de alavancar a venda do LEITE CONDENSADO que é comprado apenas 0,11% das vezes:
* se colocarmos leite condesado próximo ao leite;
* montar promomoções na compra de duas caixa de leite o cliente ganha um desconto no leite condensado;
* montar Kit de vendas

:pushpin: Essas ideias podem ser aplicadas entre os items A e items B que aparecem na tabela acima

Para entendermos melhor um pouco de como a métrica Lift se comporta podemos ver a matriz abaixo:

![Matriz](https://github.com/rafaelfabri/case/blob/main/imagens/matriz.png)

* **Lift <= 1** isso mostra que não temos evidencias suficientes que o cliente que fazer aquisição do item A também vai fazer a do item B.
* **Lift > 1** isso mostra indicios que a aquisição do item A aumenta a chance da aquisição do item B.

Para chegarmos nesses resultados do Lift tem 4 possibilidades:
1) ( :arrow_up: Confidence Alto) e ( :arrow_down: Support Alto): Quando se tem a condidence(P(B|A)) alto isso indica que existe uma grande probabilidade do item B ser adiquirido quando o item A também for. No entanto, o item B isoladamente já possui uma alta probabilidade de aquisição. Portanto, não há um questão de associação entre o item A e o item B, mas sim uma semelhança por os dois serem items que possuem alto volume de vendas.

2) ( :arrow_up: Confidence Alto) e ( :arrow_down: Support Pequeno): Esse caso representa o exemplo acima, a confidence é alta fazendo o item B ter uma alta probabilidade de ser adquirido se o item A também for adquirido. Quando olhamos isoladamente o item B há pouca pouca aquisição deste no período. No entanto, quando acompanhado do item A está na cesta a chance do item B ser comprado aumenta.

3) ( :arrow_down: Confidence Pequeno) e ( :arrow_up: Support Alto): A confidence dos dois produtos é pequena, mas o support do item B é alto, o que provoca um Lift menor que 1, o item A e B são comprados individualmente não sendo associados.

4) ( :arrow_down: Confidence Pequeno) e ( :arrow_down: Support Pequeno): Nesse caso os dois são pequenos, não há indicios suficientes para dizermos que os items são associados.

Abaixo estão os valores com menor Lift.

![exemplo 3](https://github.com/rafaelfabri/case/blob/main/imagens/tabela_final_parte_1_.png)

Observa-se que todos os Lift são maiores que 1, mas esses valores continuam próximo de 1 ainda indicando uma fraca associação. Observando o items A, nota-se que todos são cervejas e comparando com o item B, na prática, pode-se afirmar que realmente não há uma associação entre esses items. No entanto, é importante realizar um estudo com mais cuidadoso.


# Parte 2: Data Science

A análise feita na parte 2 encontra-se em um jupyter notebook neste repositório do GitHub:
case/notebooks/parte_2_data_science.ipynb
https://github.com/rafaelfabri/case/blob/main/notebooks/parte_2_data_science.ipynb

![img 1](https://github.com/rafaelfabri/case/blob/main/imagens/Algoritmo_Apriori.png)

Para a parte 2 a ideia é verificar a associação de 3 items, para isso foi proposto utilizar o algoritmo apriori. 

:pushpin: Foi feito algumas adpatações em relação ao algoritmo para simplicar a complexidade do algoritmo. Foi utilizado lógicas, loop e algoritmo para calcular as métricas do algoritmo apriori, não foi utilizada a biblioteca mlxtend pela quantidade significativa de items e pelas transformações de dados necessária iria honerar muito em processamento.

> **Fluxograma**

![img 2](https://github.com/rafaelfabri/case/blob/main/imagens/fluxograma_apriori.png)

Para o algoritmo apriori é necessário colocar um limite como valor de corte para retirar produtos que não possuem um Support tão alto e diminuirmos a complexidade do algoritmo. Pensando em simplificar a primeira parte do algoritmo foi feito semelhante a etapa anterior, foi pego os 10 items mais relevantes pela métrica support(P(A)) invés de aplicar o limite. Com esses 10 items foi calculado o Support(P(A,B)) e depois Support(P(A,B,C))  

$$Support(P(A,B)) = \frac{qtd cestas com (A and B)}{n}$$

$$Support(P(A,B)) = \frac{qtd cestas com (A and B and C)}{n}$$


> **Resultados**

![img 3](https://github.com/rafaelfabri/case/blob/main/imagens/apriori_1.png)

![img 4](https://github.com/rafaelfabri/case/blob/main/imagens/apriori_2.png)

![img 5](https://github.com/rafaelfabri/case/blob/main/imagens/apriori_3.png)


# Parte 3: Pipeline de dados

![img 6](https://github.com/rafaelfabri/case/blob/main/imagens/airflow.png)

O pipeline de dados da parte 3 encontra-se em um script .py neste repositório do GitHub:
case/airflow/dags/parte_3_airflow.py
https://github.com/rafaelfabri/case/blob/main/airflow/dags/parte_3_airflow.py

Para realizar a orquestração em Airflow foi criada a DAG com o nome algoritmo_apriori, com três Tasks como mostrado abaixo:

![img 7](https://github.com/rafaelfabri/case/blob/main/imagens/airflow_dag.png)

![img 8](https://github.com/rafaelfabri/case/blob/main/imagens/airflow_tasks.png)

Foi utilizado uma Task vazia, chamada de Inicio apenas para representar o início do código.

Depois existe uma Task chamada extracao_dados_e_execucao_apriori. Essa task possui algumas funções dentro dela, a principal é realizar a extração de dados e depois realizar as etapas do algoritimo apriori.

:pushpin: Não foi escolhido fazer duas tasks individuais para extraçao e execuçao do algoritmo, pois para passar o dataframe de uma task para outra utilizando um *XCOM* ou fazendo um carregamento, pode honerar muito por estarmos trabalhando com um volume significativo de dados.

A task final utiliza de XCOM para salvar o arquivo localmente já que é um dataframe consolidado menor.

Para respondermos a pergunta 2 da parte 3 para gravar a saída do algoritmo apriori para uma tabela no BigQuery, pode-se substituir a task 3 pelo código abaixo. Nunca trabalhei com BigQuery então não tenho certeza se toda sintaxe esta correta.


```python
	    PROJECT = ''
	    DESTINATION_DS = ''
	    DESTINATION_TBL = ''
	    
	    load_data = BigQueryInsertJobOperator(task_id='copy-table-1',
		                                  configuration={
		                                        'query': {
		                                            'query': open('my.sql', 'r').read().format(**locals()),
		                                            'destinationTable': {
		                                                'projectId': PROJECT,
		                                                'datasetId': DESTINATION_DS,
		                                                'tableId': DESTINATION_TBL
		                                            },
		                                            'useLegacySql': False,
		                                            'allowLargeResults': True,
		                                        }
		                                    },
		                                    dag=dag
		                                )) 
``
