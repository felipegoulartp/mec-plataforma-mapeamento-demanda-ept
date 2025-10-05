# src/data_processing/load_censo.py

import pandas as pd

def processar_dados_censo(caminho_arquivo_csv):
    """
    Lê o arquivo CSV JÁ PROCESSADO do Censo Escolar para Minas Gerais.
    """
    try:
        # Apenas lemos o arquivo, pois ele já está limpo e filtrado.
        df_censo_limpo = pd.read_csv(caminho_arquivo_csv, sep=';', encoding='utf-8-sig')
        
        print("Dados do Censo Escolar (processados) carregados com sucesso.")
        return df_censo_limpo

    except FileNotFoundError:
        print(f"ERRO: Arquivo do Censo (CSV) não encontrado em '{caminho_arquivo_csv}'")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao carregar os dados do Censo: {e}")
        return None