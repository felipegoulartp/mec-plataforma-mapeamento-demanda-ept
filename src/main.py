# src/main.py

import pandas as pd
from unidecode import unidecode
import numpy as np

# Importa as funções de processamento que criamos
from data_processing.load_caged import processar_dados_caged
from data_processing.load_ibge import processar_dados_ibge
from data_processing.load_censo import processar_dados_censo

print("Iniciando pipeline de análise integrada...")

# --- ETAPA 1: CARREGAR DADOS ---
caminho_caged_raw = 'data/raw/3-tabelas_Agosto de 2025.xlsx'
caminho_ibge_raw = 'data/raw/Agregados_por_municipios_alfabetizacao_BR.csv'
caminho_censo_proc = 'data/processed/censo_escolar_mg_limpo.csv'

df_demanda = processar_dados_caged(caminho_caged_raw)
df_publico = processar_dados_ibge(caminho_ibge_raw)
df_oferta = processar_dados_censo(caminho_censo_proc)

# --- ETAPA 2: INTEGRAR DADOS ---
if df_demanda is not None and df_publico is not None and df_oferta is not None:
    
    def normalizar_nome(nome):
        try: return unidecode(str(nome)).upper().strip()
        except: return np.nan

    df_demanda['chave_municipio'] = df_demanda['Municipio_Nome'].apply(normalizar_nome)
    df_publico['chave_municipio'] = df_publico['Municipio_Nome'].apply(normalizar_nome)
    df_oferta['chave_municipio'] = df_oferta['Município'].apply(normalizar_nome)

    df_integrado = pd.merge(df_demanda, df_oferta, on='chave_municipio', how='inner')
    df_integrado_completo = pd.merge(df_integrado, df_publico, on='chave_municipio', how='left')
    print("Dados de Demanda, Oferta e Público-Alvo integrados com sucesso.")

    # --- ETAPA 3: CALCULAR ÍNDICE E GERAR RANKING ---
    df_integrado_completo['Total_Matriculas_EPT_calc'] = df_integrado_completo['Total_Matriculas_EPT'].replace(0, 1)
    df_integrado_completo['Indice_Oportunidade'] = (df_integrado_completo['Saldo'] / df_integrado_completo['Total_Matriculas_EPT_calc']) * 100

    df_analise = df_integrado_completo[[
        'Município', 'Saldo', 'Total_Matriculas_EPT', 'Populacao_15_a_19', 'Indice_Oportunidade'
    ]].copy()
    df_analise['Indice_Oportunidade'] = df_analise['Indice_Oportunidade'].round(2)
    
    print("\n--- RANKING DE OPORTUNIDADE PARA EPT EM MINAS GERAIS ---")
    print("Cidades com maior demanda de empregos em relação à oferta de matrículas.\n")
    
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    
    # CORREÇÃO FINAL: Usando print() em vez de display()
    print(df_analise.sort_values(by='Indice_Oportunidade', ascending=False).head(30))
    
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')

else:
    print("\nERRO: Uma ou mais fontes de dados não puderam ser carregadas. A análise não pode continuar.")