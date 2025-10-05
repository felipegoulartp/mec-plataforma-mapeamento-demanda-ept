# src/analysis/opportunity_index.py
import pandas as pd
from unidecode import unidecode
import numpy as np

def normalizar_nome(nome):
    try:
        return unidecode(str(nome)).upper().strip()
    except:
        return np.nan

def calcular_indice_e_ranking(df_demanda, df_publico, df_oferta):
    if df_demanda is None or df_publico is None or df_oferta is None:
        return None

    # Criamos a chave de unificação em cada tabela
    df_demanda['chave_municipio'] = df_demanda['Municipio_Nome'].apply(normalizar_nome)
    df_publico['chave_municipio'] = df_publico['Municipio_Nome'].apply(normalizar_nome)
    df_oferta['chave_municipio'] = df_oferta['Município'].apply(normalizar_nome)

    # Unimos (merge) as tabelas em cascata
    df_integrado = pd.merge(df_demanda, df_oferta, on='chave_municipio', how='inner')
    df_integrado_completo = pd.merge(df_integrado, df_publico, on='chave_municipio', how='left')

    # Calculamos o índice
    df_integrado_completo['Total_Matriculas_EPT_calc'] = df_integrado_completo['Total_Matriculas_EPT'].replace(0, 1)
    df_integrado_completo['Indice_Oportunidade'] = (df_integrado_completo['Saldo'] / df_integrado_completo['Total_Matriculas_EPT_calc']) * 100

    # Selecionamos e renomeamos as colunas
    df_analise = df_integrado_completo[[
        'Município', 'Saldo', 'Total_Matriculas_EPT', 'Populacao_15_a_19', 'Indice_Oportunidade'
    ]].copy()
    df_analise['Indice_Oportunidade'] = df_analise['Indice_Oportunidade'].round(2)
    
    # Ordenamos o resultado
    df_analise_final = df_analise.sort_values(by='Indice_Oportunidade', ascending=False)
    
    return df_analise_final