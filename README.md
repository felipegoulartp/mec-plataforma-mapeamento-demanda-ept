# 🗺️ Plataforma de Mapeamento da Demanda por EPTNM

**Proponente:** Universidade Federal de Uberlândia (UFU)  
**Edital de Referência:** [Edital Nº 5/2025 - MEC/SETEC](https://www.gov.br/mec/pt-br/juros-por-educacao/edital-demanda-por-qualificacao-profissional)

---

## 📍 1. Sobre o Projeto

Este repositório apresenta o protótipo funcional da **Plataforma Integrada para Mapeamento da Demanda por Educação Profissional Técnica de Nível Médio (EPTNM)**. O projeto foi desenvolvido como uma ferramenta de apoio à implementação do **Programa Juros por Educação**, em resposta à Chamada Pública do Ministério da Educação (MEC).

O objetivo é fornecer um instrumento de código aberto, robusto e replicável para auxiliar gestores públicos e instituições de ensino a planejar a oferta de cursos técnicos. A análise busca alinhar a formação profissional às necessidades reais do mercado de trabalho, a partir da integração de dados de fontes governamentais abertas.

O protótipo atual oferece uma interface web interativa para explorar os dados de **Minas Gerais**, permitindo análises dinâmicas através de filtros e visualizações geoespaciais.

---

## 🎯 2. Objetivos da Plataforma

### Objetivo Geral
Desenvolver uma plataforma digital aberta e interoperável para mapear a demanda por cursos técnicos de nível médio, através do cruzamento de dados sobre mercado de trabalho, perfil populacional e oferta educacional.

### Objetivos Específicos
- **Identificar** tendências de demanda por mão de obra a nível municipal.
- **Mapear** o perfil do público-alvo potencial para a EPTNM em diferentes faixas etárias.
- **Diagnosticar** a oferta atual de matrículas na rede de ensino técnico.
- **Prover** indicadores sintéticos que revelem lacunas entre oferta e demanda, gerando insights para investimentos.
- **Atender** integralmente às oito dimensões de dados exigidas pelo Edital nº 5/2025.

---

## 🔧 3. Metodologia e Arquitetura

A plataforma foi construída com base em um pipeline de dados modular em Python, utilizando bibliotecas de código aberto para garantir a performance e a replicabilidade.

- **Linguagem Principal:** `Python 3.10`

- **Análise e Processamento de Dados (ETL):**
  - **Pandas:** Para manipulação e limpeza dos dados tabulares.
  - **GeoPandas:** Para processamento dos dados geoespaciais dos municípios.
  - *A metodologia incluiu a superação de desafios como a leitura de arquivos Excel com formatação complexa (cabeçalhos de múltiplos níveis do CAGED) e a normalização de nomes de municípios entre diferentes fontes de dados.*

- **Visualização e Dashboard:**
  - **Streamlit:** Para a construção rápida e eficiente da aplicação web interativa.
  - **Plotly Express:** Para a criação de visualizações de dados ricas, como o mapa coroplético e os gráficos de barras interativos.

- **Indicadores-Chave Desenvolvidos:**
  - **🎯 Índice de Oportunidade:** `(Saldo de Vagas / Total Matrículas EPT) * 100`. Cruza a demanda do mercado com a oferta educacional. Um índice alto sugere uma forte oportunidade para novos cursos.
  - **📊 Índice de Demanda por Público:** `(Saldo de Vagas / População na Faixa Etária) * 1000`. Mede a pressão do mercado de trabalho sobre a população local. Responde à pergunta: *"Para cada 1.000 pessoas nesta faixa etária, quantas vagas líquidas foram criadas?"*.

---

## 📂 4. Estrutura do Repositório

O projeto está organizado para separar claramente a lógica de processamento de dados da aplicação de visualização.

📄 app.py: O script principal que executa a aplicação Streamlit.

📦 requirements.txt: A lista de todas as dependências Python necessárias.

📂 data/: Pasta que contém todos os dados.

   - raw/: Armazena os arquivos de dados originais, como foram baixados.

   - processed/: Armazena os arquivos já limpos e preparados para a análise.

📂 notebooks/: Contém os Jupyter Notebooks usados para exploração e testes.

📂 src/: Guarda o código-fonte modularizado da aplicação.

   - data_processing/: Módulos para carregar e limpar os dados.

   - analysis/: Módulos para calcular os indicadores.

📄 README.md: Este documento de apresentação.

## 🚀 5. Como Executar o Protótipo

Para executar a aplicação localmente, siga os passos abaixo.

### Pré-requisitos
- **Python 3.10** ou superior instalado.
- **Git** instalado.

### Passos para Execução

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/felipegoulartp/mec-plataforma-mapeamento-demanda-ept](https://github.com/felipegoulartp/mec-plataforma-mapeamento-demanda-ept)
    cd seu-repositorio
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

## 📜 6. Licença

Este projeto é disponibilizado em conformidade com o **item 1.8 do Edital Nº 5/2025**. O conteúdo pode ser utilizado e compartilhado para fins não comerciais, desde que o trabalho seja distribuído inalterado, na íntegra, e com o devido crédito aos autores.

---

## 🧑‍💻 7. Contato e Responsáveis

-   **Vivian Consuelo Reolon Schmidt** - *Docente e Orientadora*
-   **Felipe Goulart Pereira** - *Discente e Desenvolvedor*
