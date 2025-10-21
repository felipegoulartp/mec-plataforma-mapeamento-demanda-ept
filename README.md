# 🗺️ Plataforma de Mapeamento da Demanda por EPTNM

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red.svg)
![License](https://img.shields.io/badge/Licen%C3%A7a-Uso%20N%C3%A3o%20Comercial-lightgrey.svg)

**Proponente:** Universidade Federal de Uberlândia (UFU)  
**Edital de Referência:** [Edital Nº 5/2025 - MEC/SETEC](https://www.gov.br/mec/pt-br/juros-por-educacao/edital-demanda-por-qualificacao-profissional)

---

## 📍 1. Sobre o Projeto

Este repositório apresenta o protótipo funcional da **Plataforma Integrada para Mapeamento da Demanda por Educação Profissional Técnica de Nível Médio (EPTNM)**. O projeto foi desenvolvido como uma ferramenta de apoio à implementação do **Programa Juros por Educação**, em resposta à Chamada Pública do Ministério da Educação (MEC).

O objetivo é fornecer um instrumento de código aberto, robusto e replicável para auxiliar gestores públicos e instituições de ensino a planejar a oferta de cursos técnicos. A análise busca alinhar a formação profissional às necessidades reais do mercado de trabalho, a partir da integração de dados de fontes governamentais abertas.

O protótipo atual (`app.py`) oferece uma interface web interativa para explorar os dados de **Minas Gerais**, permitindo análises dinâmicas através de filtros e visualizações geoespaciais.

---

## 🖥️ 2. Preview do Protótipo

Interface principal da plataforma (`app.py`) em execução, demonstrando o mapa coroplético de Minas Gerais e indicadores-chave.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5b625ffb-7375-4942-b449-8c3aa58c4025" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4141bcc0-107d-45de-aac0-721439281492" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4c3090d2-fa03-4ee6-97d2-c69e92fef0a7" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/14946385-cf96-42ea-af09-c8cf50f8ac41" />

---

## 🎯 3. Objetivos da Plataforma

### Objetivo Geral
Desenvolver uma plataforma digital aberta e interoperável para mapear a demanda por cursos técnicos de nível médio, através do cruzamento de dados sobre mercado de trabalho, perfil populacional e oferta educacional.

### Objetivos Específicos
- **Identificar** tendências de demanda por mão de obra a nível municipal.
- **Mapear** o perfil do público-alvo potencial para a EPTNM em diferentes faixas etárias.
- **Diagnosticar** a oferta atual de matrículas na rede de ensino técnico.
- **Prover** indicadores sintéticos que revelem lacunas entre oferta e demanda, gerando insights para investimentos.
- **Atender** integralmente às oito dimensões de dados exigidas pelo Edital nº 5/2025.

---

## 📊 4. Fontes de Dados

A metodologia desta plataforma baseia-se na integração e cruzamento de três pilares de dados públicos abertos, todos presentes na pasta `/data/raw/`:

- 🏭 **Demanda (Ministério do Trabalho):** Dados do Novo CAGED.
  - *Arquivo:* `3-tabelas_Agosto de 2025.xlsx`
  - *Análise:* Foco no saldo de vagas formais (Admissões - Desligamentos) para medir a demanda do mercado.

- 👨‍👩‍👧‍👦 **Público-Alvo (IBGE):** Dados do Censo Demográfico 2022.
  - *Arquivo:* `Agregados_por_municipios_alfabetizacao_BR.csv`
  - *Análise:* Foco na população em idade escolar (ex: 15-19 anos) como público-alvo potencial.

- 🎓 **Oferta (MEC/INEP):** Dados do Censo Escolar 2023.
  - *Arquivo:* `censo_escolar_2023.xlsx`
  - *Análise:* Foco no total de matrículas em Educação Profissional Técnica (EPT) para medir a oferta atual.

- 🗺️ **Geografia (IBGE):** Malhas municipais de Minas Gerais.
  - *Arquivo:* `geojs-31-mun.json`
  - *Análise:* Utilizado para a renderização do mapa coroplético.

---

## 🔧 5. Metodologia e Arquitetura

A plataforma foi construída com base em um pipeline de dados modular em Python, utilizando bibliotecas de código aberto para garantir a performance e a replicabilidade.

- **Linguagem Principal:** `Python 3.10`

- **Análise e Processamento de Dados (ETL):**
  - **Pandas:** Para manipulação e limpeza dos dados tabulares.
  - **GeoPandas:** Para processamento dos dados geoespaciais.
  - **Unidecode:** Para a normalização robusta de nomes de municípios entre diferentes fontes de dados (ex: "Mg-Belo Horizonte" vs "Belo Horizonte").
  - *A metodologia superou desafios como a leitura de arquivos Excel com formatação complexa (cabeçalhos de múltiplos níveis do CAGED) e a junção segura de fontes heterogêneas.*

- **Visualização e Dashboard:**
  - **Streamlit:** Para a construção rápida e eficiente da aplicação web interativa (`app.py`).
  - **Plotly Express:** Para a criação de visualizações de dados ricas, como o mapa coroplético e os gráficos de barras interativos.

- **Indicadores-Chave Desenvolvidos:**
  - **🎯 Índice de Oportunidade:** `(Saldo de Vagas / Total Matrículas EPT) * 100`. Cruza a demanda do mercado com a oferta educacional. Um índice alto sugere uma forte oportunidade para novos cursos.
  - **📊 Índice de Demanda por Público:** `(Saldo de Vagas / População na Faixa Etária) * 1000`. Mede a pressão do mercado de trabalho sobre a população local. Responde à pergunta: *"Para cada 1.000 pessoas nesta faixa etária, quantas vagas líquidas foram criadas?"*.

---

## 📂 6. Estrutura do Repositório

O projeto está organizado para separar claramente a lógica de processamento de dados da aplicação de visualização.

* 📄 `app.py`: Script principal da aplicação Streamlit.
* 📄 `requirements.txt`: Lista de dependências Python.
* 📄 `gerar_reqs.py`: Script utilitário para criar o `requirements.txt`.
* 📄 `README.md`: Este documento de apresentação.
* 📂 `data/`: Pasta que contém todos os dados.
    * `raw/`: Armazena os arquivos de dados originais (CAGED, IBGE, Censo Escolar, GeoJSON).
    * `processed/`: Armazena os arquivos já limpos e preparados para a análise (ex: `censo_escolar_mg_limpo.csv`).
* 📂 `notebooks/`: Contém os Jupyter Notebooks usados para exploração e testes.
    * `01_analise_caged.ipynb`: Análise exploratória dos dados do CAGED.
    * `02_analise_demografica_ibge.ipynb`: Análise exploratória dos dados do IBGE.
    * `03_analise_cruzada_caged_ibge.ipynb`: Notebook para cruzamento e limpeza dos dados do CAGED e IBGE.
    * `04_analise_censo_escolar.ipynb`: Análise exploratória dos dados do Censo Escolar.
* 📂 `src/`: Guarda o código-fonte modularizado da aplicação.
    * `data_processing/`: Módulos para carregar e limpar os dados (ex: `load_caged.py`, `load_ibge.py`).
    * `analysis/`: Módulos para calcular os indicadores (ex: `opportunity_index.py`).

---

## 🚀 7. Como Executar o Protótipo

Para executar a aplicação localmente, siga os passos abaixo.

### Pré-requisitos
- **Python 3.10** ou superior instalado.
- **Git** instalado.

### Passos para Execução

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/felipegoulartp/mec-plataforma-mapeamento-demanda-ept](https://github.com/felipegoulartp/mec-plataforma-mapeamento-demanda-ept)
    cd mec-plataforma-mapeamento-demanda-ept
    ```

2.  **Crie e ative um ambiente virtual (Recomendado):**
    ```bash
    # Comando para criar o ambiente
    python -m venv .venv

    # No Windows (PowerShell)
    .\.venv\Scripts\activate

    # No macOS/Linux
    source .venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação Streamlit:**
    ```bash
    streamlit run app.py
    ```
Após executar o comando, uma nova aba será aberta automaticamente no seu navegador com o protótipo funcional.

---

## 📜 8. Licença

Este projeto é disponibilizado em conformidade com o **item 1.8 do Edital Nº 5/2025**. O conteúdo pode ser utilizado e compartilhado para fins não comerciais, desde que o trabalho seja distribuído inalterado, na íntegra, e com o devido crédito aos autores.

---

## 🧑‍💻 9. Contato e Responsáveis

- **Vivian Consuelo Reolon Schmidt** - *Docente e Orientadora*
- **Felipe Goulart Pereira** - *Discente e Desenvolvedor*
