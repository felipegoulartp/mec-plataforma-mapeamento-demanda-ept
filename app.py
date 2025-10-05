# app.py

import streamlit as st
import pandas as pd
from src.data_processing.load_caged import processar_dados_caged
from src.data_processing.load_ibge import processar_dados_ibge
from src.data_processing.load_censo import processar_dados_censo
from src.analysis.opportunity_index import calcular_indice_e_ranking

# --- Configuração da Página ---
st.set_page_config(
    page_title="Mapeamento de Demandas EPT",
    page_icon="📊",
    layout="wide"
)

# --- Título e Descrição ---
st.title("📊 Protótipo: Mapeamento de Oportunidades para Educação Profissional")
st.markdown("""
Esta ferramenta integra dados de Demanda de empregos (CAGED), Público-Alvo (IBGE) e Oferta de matrículas (Censo Escolar)
para identificar os municípios com maior potencial para expansão da Educação Profissional e Técnica (EPT) em Minas Gerais.
""")

# --- Carregamento e Processamento dos Dados ---
@st.cache_data
def carregar_dados_integrados():
    caminho_caged_raw = 'data/raw/3-tabelas_Agosto de 2025.xlsx'
    caminho_ibge_raw = 'data/raw/Agregados_por_municipios_alfabetizacao_BR.csv'
    caminho_censo_proc = 'data/processed/censo_escolar_mg_limpo.csv'

    df_demanda = processar_dados_caged(caminho_caged_raw)
    df_publico = processar_dados_ibge(caminho_ibge_raw)
    df_oferta = processar_dados_censo(caminho_censo_proc)

    df_analise_final = calcular_indice_e_ranking(df_demanda, df_publico, df_oferta)
    
    return df_analise_final

# --- Exibição dos Resultados ---
st.header("Ranking de Oportunidade por Município")

df_resultado = carregar_dados_integrados()

if df_resultado is not None:
    st.dataframe(df_resultado)
else:
    st.error("Ocorreu um erro ao carregar e processar os dados.")