# app.py

import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px
from unidecode import unidecode
import numpy as np

# Importa as funções de todos os nossos módulos de processamento, incluindo a nova de dados históricos
from src.data_processing.load_caged import processar_dados_caged, processar_caged_historico_municipal
from src.data_processing.load_ibge import processar_dados_ibge
from src.data_processing.load_censo import processar_dados_censo
from src.analysis.opportunity_index import calcular_indice_e_ranking

st.set_page_config(page_title="Mapeamento de Demandas EPT", page_icon="🗺️", layout="wide")

# --- REFINAMENTO CSS ---
st.markdown("""
<style>
    .stDataFrame { background-color: #FFFFFF; border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1); border: 1px solid #E0E0E0; }
    .stPlotlyChart { border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1); border: 1px solid #E0E0E0; background-color: #FFFFFF; padding: 10px; }
    .stDataFrame table { color: #333333; }
</style>
""", unsafe_allow_html=True)

# --- DESCRIÇÃO DETALHADA DO PROTÓTIPO ---
st.title("🗺️ Protótipo: Mapeamento de Oportunidades para Educação Profissional")
st.markdown("""
**Bem-vindo à Ferramenta de Análise de Demanda por Educação Profissional e Técnica (EPT).**

Este protótipo foi desenvolvido como uma prova de conceito para o **Edital nº 5/2025 do MEC**, com o objetivo de demonstrar uma metodologia robusta para apoiar a tomada de decisão na expansão da oferta de cursos técnicos em **Minas Gerais**. 

A ferramenta realiza uma análise integrada de três pilares de dados públicos:
- 🏭 **Demanda:** Saldo de empregos formais do Novo CAGED.
- 🎓 **Oferta:** Matrículas em cursos técnicos do Censo Escolar.
- 👨‍👩‍👧‍👦 **Público-Alvo:** Perfil demográfico do Censo IBGE.

Utilize os filtros na barra lateral para explorar os dados, identificar municípios com alto potencial e analisar os indicadores-chave gerados pela plataforma.
""")

# --- FUNÇÕES DE CARREGAMENTO (COM CACHE) ---
@st.cache_data
def carregar_dados_principais():
    caminho_caged_raw = 'data/raw/3-tabelas_Agosto de 2025.xlsx'
    caminho_ibge_raw = 'data/raw/Agregados_por_municipios_alfabetizacao_BR.csv'
    caminho_censo_proc = 'data/processed/censo_escolar_mg_limpo.csv'
    caminho_mapa = 'data/raw/geojs-31-mun.json'

    df_demanda = processar_dados_caged(caminho_caged_raw)
    df_publico = processar_dados_ibge(caminho_ibge_raw)
    df_oferta = processar_dados_censo(caminho_censo_proc)

    if df_demanda is None or df_publico is None or df_oferta is None: 
        return None

    df_analise = calcular_indice_e_ranking(df_demanda, df_publico, df_oferta)
    
    gdf_mapa = gpd.read_file(caminho_mapa)
    df_analise['Código do Município'] = df_analise['Código do Município'].astype(str)
    gdf_mapa['id'] = gdf_mapa['id'].astype(str)
    df_mapa_final = gdf_mapa.merge(df_analise, left_on='id', right_on='Código do Município', how='left')
    
    return df_mapa_final

@st.cache_data
def carregar_dados_historicos():
    caminho_caged_raw = 'data/raw/3-tabelas_Agosto de 2025.xlsx'
    return processar_caged_historico_municipal(caminho_caged_raw)

df_mapa = carregar_dados_principais()
df_historico = carregar_dados_historicos()

# --- BARRA LATERAL COM FILTROS ---
st.sidebar.image("https://www.gov.br/mec/pt-br/assuntos/noticias/imagens/2023/junho/iniciativa-do-mec-leva-carreta-escola-para-cursos-de-formacao-profissional-em-minas-gerais/imagem-divulgacao.jpg/@@images/image", use_container_width=True)
st.sidebar.title("Painel de Controle")
st.sidebar.markdown("Use os filtros para refinar a análise.")

if df_mapa is not None and not df_mapa.empty:
    faixa_etaria_map = { 
        "Todas as faixas (15 a 29)": "Populacao_Todas_as_faixas",
        "15 a 19 anos": "Populacao_15_a_19", 
        "20 a 24 anos": "Populacao_20_a_24", 
        "25 a 29 anos": "Populacao_25_a_29" 
    }
    faixa_selecionada_label = st.sidebar.selectbox("👤 **Público-Alvo:**", options=list(faixa_etaria_map.keys()))
    coluna_populacao_selecionada = faixa_etaria_map[faixa_selecionada_label]

    faixas_populacao = {
        "Todos os portes": (0, df_mapa[coluna_populacao_selecionada].max()), 
        "Até 1.000 pessoas": (0, 1000), 
        "De 1.001 a 5.000 pessoas": (1001, 5000), 
        "De 5.001 a 20.000 pessoas": (5001, 20000), 
        "Acima de 20.000 pessoas": (20001, df_mapa[coluna_populacao_selecionada].max())
    }
    faixa_pop_selecionada_label = st.sidebar.selectbox("🏘️ **Porte do Município:**", options=list(faixas_populacao.keys()))
    min_pop, max_pop = faixas_populacao[faixa_pop_selecionada_label]
    
    df_filtrado = df_mapa[ (df_mapa[coluna_populacao_selecionada].fillna(0) >= min_pop) & (df_mapa[coluna_populacao_selecionada].fillna(0) <= max_pop) ]
    
    df_filtrado.loc[:, 'Populacao_calc'] = df_filtrado[coluna_populacao_selecionada].replace(0, 1)
    df_filtrado.loc[:, 'Indice_Demanda_por_Publico'] = (df_filtrado['Saldo'] / df_filtrado['Populacao_calc']) * 1000
    df_filtrado.loc[:, 'Indice_Demanda_por_Publico'] = df_filtrado['Indice_Demanda_por_Publico'].round(2)

else:
    df_filtrado = None

# --- EXIBIÇÃO DOS RESULTADOS ---
if df_filtrado is not None and not df_filtrado.empty:
    st.header("Análise Integrada de Oportunidades")
    fig_mapa = px.choropleth_mapbox(df_filtrado, geojson=df_filtrado.geometry, locations=df_filtrado.index, color="Indice_Oportunidade", center={"lat": -18.5, "lon": -44.5}, mapbox_style="carto-positron", zoom=5, hover_name="Município", hover_data={'Saldo': True, 'Total_Matriculas_EPT': True, 'Indice_Oportunidade': ':.2f', 'Indice_Demanda_por_Publico': ':.2f'}, color_continuous_scale="RdYlBu_r", opacity=0.7, labels={'Indice_Oportunidade': 'Índice de Oportunidade'})
    st.plotly_chart(fig_mapa, use_container_width=True)

    st.header("Ranking Detalhado por Município")
    with st.expander("Clique aqui para entender os conceitos e o significado de cada coluna"):
        st.markdown("""
        - 🏙️ **Município:** Nome do município em Minas Gerais.
        - <span style='color: #2E86C1;'>📈 **Saldo:**</span> (Indicador de **DEMANDA**) Balanço de empregos formais (Admissões - Desligamentos) no acumulado do ano.
        - <span style='color: #2ECC71;'>🎓 **Total Matrículas EPT:**</span> (Indicador de **OFERTA**) Total de matrículas em cursos de Educação Profissional e Técnica.
        - <span style='color: #F39C12;'>👨‍👩‍👧‍👦 **População (faixa etária):**</span> (Indicador de **PÚBLICO-ALVO**) Contingente populacional na faixa etária selecionada.
        - <span style='color: #8E44AD;'>🎯 **Índice de Oportunidade:**</span> (OFERTA vs. DEMANDA) Métrica que cruza a demanda do mercado com a oferta educacional. Um **índice alto** sugere uma forte oportunidade para novos cursos.
        - <span style='color: #C0392B;'>📊 **Índice Demanda/Público:**</span> (DEMANDA vs. PÚBLICO-ALVO) Métrica que mede a pressão do mercado sobre a população local.
        """, unsafe_allow_html=True)
        
    colunas_para_exibir = ['Município', 'Saldo', 'Total_Matriculas_EPT', coluna_populacao_selecionada, 'Indice_Oportunidade', 'Indice_Demanda_por_Publico']
    df_para_exibir = df_filtrado.sort_values(by='Indice_Oportunidade', ascending=False)[colunas_para_exibir]
    df_para_exibir.rename(columns={'Total_Matriculas_EPT': 'Total Matrículas EPT', 'Indice_Oportunidade': 'Índice de Oportunidade', coluna_populacao_selecionada: f'População ({faixa_selecionada_label})', 'Indice_Demanda_por_Publico': 'Índice Demanda/Público'}, inplace=True)
    st.dataframe(df_para_exibir.dropna(subset=['Município']))

    st.header("Visualizações em Destaque")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Top 15 - Índice de Oportunidade")
        st.markdown("Destaca os municípios onde a **demanda (saldo de vagas) mais supera a oferta educacional (matrículas)**.")
        df_grafico_1 = df_para_exibir.dropna(subset=['Município']).head(15)
        if not df_grafico_1.empty:
            fig1 = px.bar(df_grafico_1.sort_values(by='Índice de Oportunidade', ascending=True), x='Índice de Oportunidade', y='Município', orientation='h', color='Índice de Oportunidade', color_continuous_scale='Blues')
            fig1.update_layout(plot_bgcolor='white', yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        st.subheader("Top 15 - Índice Demanda/Público")
        st.markdown("Destaca os municípios onde o **mercado de trabalho está mais aquecido em proporção ao público-alvo**.")
        df_grafico_2 = df_para_exibir.sort_values(by='Índice Demanda/Público', ascending=False).dropna(subset=['Município']).head(15)
        if not df_grafico_2.empty:
            fig2 = px.bar(df_grafico_2.sort_values(by='Índice Demanda/Público', ascending=True), x='Índice Demanda/Público', y='Município', orientation='h', color='Índice Demanda/Público', color_continuous_scale='Reds')
            fig2.update_layout(plot_bgcolor='white', yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig2, use_container_width=True)
else:
    st.error("Não foram encontrados dados para os filtros selecionados ou ocorreu um erro no processamento.")

# --- SEÇÃO DE ANÁLISE HISTÓRICA ---
st.divider()
st.header("📈 Análise da Tendência Histórica por Município")
st.info("Selecione um município da lista (que respeita os filtros aplicados acima) para visualizar a evolução mensal do saldo de vagas nos últimos anos (Fonte: CAGED Tabela 8.1).")

if df_historico is not None and df_filtrado is not None and not df_filtrado.empty:
    lista_municipios_historico = sorted(df_filtrado['Município'].dropna().unique())
    
    if lista_municipios_historico:
        municipio_selecionado = st.selectbox("Selecione um município para análise histórica:", options=lista_municipios_historico)

        if municipio_selecionado:
            chave_selecionada = unidecode(str(municipio_selecionado)).upper().strip()
            dados_historico_municipio = df_historico[df_historico['chave_municipio'] == chave_selecionada]
            
            fig_historico = px.line(
                dados_historico_municipio.sort_values(by='Data'),
                x='Data', y='Saldo_Mensal', title=f"Evolução do Saldo de Vagas em {municipio_selecionado}",
                labels={'Data': 'Mês/Ano', 'Saldo_Mensal': 'Saldo Mensal de Vagas'}
            )
            fig_historico.add_hline(y=0, line_dash="dash", line_color="grey")
            fig_historico.update_layout(plot_bgcolor='white')
            st.plotly_chart(fig_historico, use_container_width=True)
else:
    st.warning("Não foi possível carregar os dados históricos ou nenhum município foi encontrado para a análise de tendência.")

# --- SEÇÃO DE REFERÊNCIAS ---
st.divider()
st.subheader("Fontes dos Dados e Referências")
st.markdown("""
- **Demanda de Emprego:** Novo CAGED, Ministério do Trabalho e Emprego. Períodos: Acumulado do Ano (Jan-Ago/2025) e Série Histórica (Jan/2020 a Ago/2025). Arquivo: `3-tabelas_Agosto de 2025.xlsx`.
- **Oferta Educacional:** Microdados do Censo Escolar, INEP/MEC. Período: 2023. Arquivo: `censo_escolar_2023.xlsx`.
- **Público-Alvo:** Censo Demográfico, IBGE. Período: 2022. Arquivo: `Agregados_por_municipios_alfabetizacao_BR.csv`.
- **Dados Geográficos:** IBGE, via [GitHub/tbrugz](https://github.com/tbrugz/geodata-br/raw/master/geojson/geojs-31-mun.json).
""")

