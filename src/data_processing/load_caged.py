# src/data_processing/load_caged.py
import pandas as pd
import locale

# Tenta configurar o locale para português para ler os nomes dos meses corretamente.
try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil')
    except locale.Error:
        print("Aviso: Não foi possível configurar o locale para português. A conversão de datas pode falhar.")

def processar_dados_caged(caminho_arquivo):
    """
    Lê a Tabela 3 do arquivo CAGED para extrair o Saldo total de empregos
    do Acumulado do Ano para cada município de Minas Gerais.
    """
    try:
        df_caged_raw = pd.read_excel(caminho_arquivo, sheet_name='Tabela 3', header=[4, 5])
        df_caged_mg = df_caged_raw[df_caged_raw[('UF', 'Unnamed: 1_level_1')] == 'MG'].copy()
        df_demanda = df_caged_mg[[
            ('Município', 'Unnamed: 3_level_1'),
            ('Acumulado do Ano (2025) - com ajuste', 'Saldos')
        ]].copy()
        df_demanda.columns = ['Municipio_Nome', 'Saldo']
        df_demanda['Municipio_Nome'] = df_demanda['Municipio_Nome'].str.replace('Mg-', '', regex=False).str.strip()
        print("Dados do CAGED (Saldo Total) processados com sucesso.")
        return df_demanda
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao processar o Saldo Total do CAGED: {e}")
        return None

def processar_caged_historico_municipal(caminho_arquivo):
    """
    Lê a Tabela 8.1 do arquivo CAGED, que contém a série histórica mensal
    de saldo por município, e a transforma em um formato longo e usável.
    """
    try:
        df_bruto = pd.read_excel(caminho_arquivo, sheet_name='Tabela 8.1', header=[4, 5])
        
        # CORREÇÃO: Usando os nomes exatos das colunas com '\n' que investigamos
        df_mg = df_bruto[df_bruto[('\nUF', 'Unnamed: 1_level_1')] == 'MG'].copy()
        
        coluna_municipio_original = ('\nMunicípio', 'Unnamed: 3_level_1')
        df_mg.loc[:, coluna_municipio_original] = df_mg[coluna_municipio_original].str.replace('Mg-', '', regex=False).str.strip()
        
        # CORREÇÃO: Usamos 'Saldos' (plural) para as colunas mensais, como investigamos
        colunas_saldo = [coluna_municipio_original] + [col for col in df_mg.columns if col[1] == 'Saldos']
        df_saldos = df_mg[colunas_saldo]

        novos_nomes = ['Municipio'] + [col[0] for col in df_saldos.columns[1:]]
        df_saldos.columns = novos_nomes

        df_longo = df_saldos.melt(id_vars=['Municipio'], var_name='Data', value_name='Saldo_Mensal')

        df_longo['Data'] = pd.to_datetime(df_longo['Data'], format='%B/%Y', errors='coerce')
        df_longo.dropna(subset=['Data'], inplace=True)

        print("Dados históricos do CAGED por município processados com sucesso.")
        return df_longo

    except Exception as e:
        print(f"Ocorreu um erro inesperado ao processar os dados históricos do CAGED: {e}")
        return None

