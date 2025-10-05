# src/data_processing/load_caged.py

import pandas as pd

def processar_dados_caged(caminho_arquivo):
    """
    Lê o arquivo de dados brutos do CAGED, processa e retorna uma tabela limpa
    com o Saldo de empregos do Acumulado do Ano para Minas Gerais.

    Args:
        caminho_arquivo (str): O caminho completo para o arquivo Excel do CAGED.

    Returns:
        pandas.DataFrame: Uma tabela contendo 'Municipio_Nome' e 'Saldo'.
    """
    try:
        # Lemos o cabeçalho de múltiplas linhas para identificar a coluna certa
        df_caged_raw = pd.read_excel(caminho_arquivo, sheet_name='Tabela 3', header=[4, 5])

        # Filtramos por MG usando o nome de coluna composto
        df_caged_mg = df_caged_raw[df_caged_raw[('UF', 'Unnamed: 1_level_1')] == 'MG'].copy()

        # Selecionamos e renomeamos as colunas de forma explícita
        df_demanda = df_caged_mg[[
            ('Município', 'Unnamed: 3_level_1'),
            ('Acumulado do Ano (2025) - com ajuste', 'Saldos')
        ]].copy()
        
        df_demanda.columns = ['Municipio_Nome', 'Saldo']
        
        # Removemos o prefixo 'Mg-' dos nomes dos municípios
        df_demanda['Municipio_Nome'] = df_demanda['Municipio_Nome'].str.replace('Mg-', '', regex=False).str.strip()

        print("Dados do CAGED processados com sucesso.")
        return df_demanda

    except FileNotFoundError:
        print(f"ERRO: Arquivo CAGED não encontrado em '{caminho_arquivo}'")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao processar os dados do CAGED: {e}")
        return None
