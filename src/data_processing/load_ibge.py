# src/data_processing/load_ibge.py
import pandas as pd

def processar_dados_ibge(caminho_arquivo):
    """
    Lê o arquivo de dados brutos do IBGE, processa e retorna uma tabela limpa
    com múltiplas faixas etárias e a soma delas para os municípios de Minas Gerais.
    """
    try:
        df_ibge_raw = pd.read_csv(caminho_arquivo, sep=';', encoding='latin-1')
        df_ibge_mg = df_ibge_raw[df_ibge_raw['CD_MUN'].astype(str).str.startswith('31')].copy()

        colunas_uteis = {
            'NM_MUN': 'Municipio_Nome', 
            'V00650': 'Populacao_15_a_19',
            'V00651': 'Populacao_20_a_24',
            'V00652': 'Populacao_25_a_29'
        }
        df_publico = df_ibge_mg[list(colunas_uteis.keys())].rename(columns=colunas_uteis).copy()

        pop_cols = ['Populacao_15_a_19', 'Populacao_20_a_24', 'Populacao_25_a_29']
        for col in pop_cols:
            df_publico[col] = pd.to_numeric(df_publico[col], errors='coerce').fillna(0).astype(int)

        # ADIÇÃO: Criamos a coluna com a soma de todas as faixas
        df_publico['Populacao_Todas_as_faixas'] = df_publico[pop_cols].sum(axis=1)

        print("Dados do IBGE (múltiplas faixas etárias) processados com sucesso.")
        return df_publico

    except Exception as e:
        print(f"Ocorreu um erro inesperado ao processar os dados do IBGE: {e}")
        return None

