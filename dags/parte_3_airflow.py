import pandas as pd 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def extracao_dados():
    
    df = pd.read_csv('/home/rafaelfabrichimidt/Documentos/Projetos/Python/codigos/case/analytics_engineer_carrefour/tutorial/CASE_PRATICO_SAMS_CLUB.csv')
    
    df['periodo'] = pd.to_datetime(df['periodo'])
    df['cesta'] = df['socio'].astype('str') + '-' + df['ticket'].astype('str')
    
    indices = df[df['item_unidade'] <= 0].index
    
    df.drop(labels = indices, axis = 0, inplace = True)
        
    
    return df


def algoritmo_apriori_items_A(df):
    
    support_A = df.groupby(['item_descricao'])['item_unidade'].sum().sort_values(ascending = False)[0:10] / df.shape[0]
    dic_support_A = dict(support_A)
    dic_support_A
    
    df_support_A = pd.DataFrame.from_dict(dic_support_A, orient = 'index')
    df_support_A.reset_index(inplace = True)
    df_support_A.columns = ['A', 'value']
    
    
    return df_support_A

def algoritmo_apriori_items_A_B(df, _10_items_mais_relevantes):
    qtd_total = df.shape[0]
    dic_support_A_B = {}
    limite = 0.0002
    
    for item in _10_items_mais_relevantes:
        
        print(item)
    
        #filtrar as cestas que possuem esse item 
        cestas = df[df['item_descricao'] == item]['cesta'].values.tolist()
        
        #filtrar apenas essas cestas
        df_cestas = df[df['cesta'].isin(cestas)].copy()
    
        #contar os items que mais aparecem nessa cesta (pegar os 15 primeiros) 
        qtd_para_confidence = df_cestas['item_descricao'].value_counts()
    
        #qtd de cestas que o item (X) aparece
        #qtd_cestas = df_cestas.shape[0]
    
        dic_uniao = dict(qtd_para_confidence / qtd_total)
    
        dic_uniao_acima_limite = {k : v for k, v in dic_uniao.items() if v > limite}
    
        dic_support_A_B[item] = dic_uniao_acima_limite
    


    df_support_A_B = pd.DataFrame.from_dict(dic_support_A_B, orient = 'index')
    colunas = df_support_A_B.columns
    df_support_A_B.reset_index(inplace = True)
    df_support_A_B.rename(columns = {'index': 'B'}, inplace = True)
    df_support_A_B = pd.melt(df_support_A_B, id_vars = 'B', value_vars = colunas)
    df_support_A_B.rename(columns = {'variable':'A'}, inplace = True)
    df_support_A_B.dropna(inplace = True)
    indices = df_support_A_B[df_support_A_B['A'] == df_support_A_B['B']].index
    df_support_A_B.drop(labels = indices, axis = 0, inplace  = True)
    df_support_A_B.reset_index(drop = True, inplace = True)
    
    return df_support_A_B



def algoritmo_apriori_items_A_B_C(df, df_support_A_B):
    limite = 0.0002
    qtd_total = df.shape[0]

    dic_support_A_B_C = {}

    for i in range(0, df_support_A_B.shape[0], 1):
        item_A = df_support_A_B.loc[i, 'A']
        item_B = df_support_A_B.loc[i, 'B']
        print('item A = {}'.format(item_A))
        print('item B = {}'.format(item_B))
    
        #filtrar as cestas que possuem esse item 
        cestas = df[(df['item_descricao'] == item_A)]['cesta'].values.tolist()
        
        #filtrar apenas essas cestas
        df_cestas = df[df['cesta'].isin(cestas)].copy()
    
        cestas = df_cestas[(df_cestas['item_descricao'] == item_B)]['cesta'].values.tolist()
    
        df_cestas = df[df['cesta'].isin(cestas)].copy()
    
        #contar os items que mais aparecem nessa cesta (pegar os 15 primeiros) 
        qtd_para_confidence = df_cestas['item_descricao'].value_counts()
            
        dic_uniao = dict(qtd_para_confidence / qtd_total)
    
        dic_uniao.pop(item_A)
        dic_uniao.pop(item_B)
            
        dic_uniao_acima_limite = {k : v for k, v in dic_uniao.items() if v > limite}
    
        dic_support_A_B_C[item_A + '-' + item_B] = dic_uniao_acima_limite

    df_support_A_B_C = pd.DataFrame.from_dict(dic_support_A_B_C, orient = 'index')
    colunas = df_support_A_B_C.columns
    
    df_support_A_B_C.reset_index(inplace = True)
    df_support_A_B_C.rename(columns = {'index': 'A-B'}, inplace = True)
    df_support_A_B_C['A'] = df_support_A_B_C['A-B'].str.split('-', expand = True)[0]
    df_support_A_B_C['B'] = df_support_A_B_C['A-B'].str.split('-', expand = True)[1]
    df_support_A_B_C.drop(labels = 'A-B', axis = 1, inplace = True)
    
    df_support_A_B_C = pd.melt(df_support_A_B_C, id_vars = ['A', 'B'], value_vars = colunas)
    df_support_A_B_C.rename(columns = {'variable':'C'}, inplace = True)
    df_support_A_B_C.dropna(inplace = True)
    
    df_support_A_B_C.reset_index(drop = True, inplace = True)
    
    return df_support_A_B_C
    

def join_tables(df_support_A, df_support_A_B, df_support_A_B_C):
    
    df_support_A['status'] = 1
    df_support_A_B['status'] = 2
    df_support_A_B_C['status'] = 3
    
    df_final = pd.concat([df_support_A, df_support_A_B, df_support_A_B_C])
    
    df_final = df_final[['A', 'B', 'C' ,'value', 'status']]
    
    df_final.reset_index(inplace = True, drop = True)
    
    df_final.fillna('', inplace = True)
    
    return df_final


df = extracao_dados()

df_support_A = algoritmo_apriori_items_A(df)

_10_items_mais_relevantes = df_support_A['A'].values.tolist()

df_support_A_B = algoritmo_apriori_items_A_B(df, _10_items_mais_relevantes)

df_support_A_B_C = algoritmo_apriori_items_A_B_C(df, df_support_A_B)

df_final = join_tables(df_support_A, df_support_A_B, df_support_A_B_C)