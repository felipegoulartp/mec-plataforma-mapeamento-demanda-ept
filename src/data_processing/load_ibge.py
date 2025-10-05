# src/data_processing/load_ibge.py

import pandas as pd

def processar_dados_ibge(caminho_arquivo):
    """
    Lê o arquivo de dados brutos do IBGE, processa e retorna uma tabela limpa
    com a população de 15 a 19 anos para os municípios de Minas Gerais.

    Args:
        caminho_arquivo (str): O caminho completo para o arquivo CSV do IBGE.

    Returns:
        pandas.DataFrame: Uma tabela contendo as colunas 'Municipio_Nome' e 'Populacao_15_a_19'.
    """
    try:
        df_ibge_raw = pd.read_csv(caminho_arquivo, sep=';', encoding='latin-1')

        # Filtra para todos os municípios de MG (código 31)
        df_ibge_mg = df_ibge_raw[df_ibge_raw['CD_MUN'].astype(str).str.startswith('31')].copy()

        # Seleciona e renomeia as colunas de interesse
        colunas_uteis = {'NM_MUN': 'Municipio_Nome', 'V00650': 'Populacao_15_a_19'}
        df_publico = df_ibge_mg[list(colunas_uteis.keys())].rename(columns=colunas_uteis).copy()

        # Garante que a coluna de população seja um número inteiro
        df_publico['Populacao_15_a_19'] = pd.to_numeric(df_publico['Populacao_15_a_19'], errors='coerce').fillna(0).astype(int)

        print("Dados do IBGE processados com sucesso.")
        return df_publico

    except FileNotFoundError:
        print(f"ERRO: Arquivo IBGE não encontrado em '{caminho_arquivo}'")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao processar os dados do IBGE: {e}")
        return None