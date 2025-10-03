# mec-plataforma-mapeamento-demanda-ept
Protótipo de plataforma para mapeamento de demandas por Educação Profissional Técnica de Nível Médio, em resposta ao Edital MEC Nº 5/2025.

# Plataforma Integrada para Mapeamento da Demanda por Educação Profissional Técnica de Nível Médio

![Banner da Plataforma](https://i.imgur.com/link-para-um-banner-visual.png)  **Proponente:** Universidade Federal de Uberlândia (UFU) <br>
[cite_start]**Edital de Referência:** [Edital Nº 5/2025 - MEC/SETEC](https://www.gov.br/mec/pt-br/acesso-a-informacao/institucional/estrutura-organizacional/orgaosespecificos-singulares/secretaria-de-educacao-profissional/editais) [cite: 144, 145] <br>
**Status do Projeto:** Em desenvolvimento (Fase de Prototipagem)

---

## 1. Sobre o Projeto

Este repositório contém o protótipo da **Plataforma Integrada para o Mapeamento da Demanda por Educação Profissional Técnica de Nível Médio (EPTNM)**. [cite_start]A proposta foi desenvolvida em resposta à Chamada Pública do Ministério da Educação (MEC), por intermédio da Secretaria de Educação Profissional e Tecnológica (Setec), para apoiar a implementação do **Programa Juros por Educação**. [cite: 5]

[cite_start]O objetivo central é fornecer uma ferramenta de código aberto, robusta e replicável que auxilie gestores públicos e instituições de ensino a planejar a oferta de cursos técnicos alinhada às necessidades reais do mundo do trabalho e aos arranjos produtivos locais e regionais. [cite: 10] [cite_start]Para isso, a plataforma consolida, integra e analisa grandes volumes de dados de fontes governamentais abertas. [cite: 321]

## 2. Objetivos da Plataforma

### Objetivo Geral
[cite_start]Desenvolver uma plataforma digital aberta e interoperável para mapear a demanda por cursos técnicos de nível médio, cruzando dados de mercado de trabalho, perfil populacional e oferta educacional. [cite: 325]

### Objetivos Específicos
1.  [cite_start]**Identificar** ocupações em crescimento e setores produtivos com maior demanda por qualificação técnica. [cite: 327]
2.  [cite_start]**Mapear** características sociodemográficas, educacionais e de vulnerabilidade social da população jovem. [cite: 328]
3.  [cite_start]**Diagnosticar** a rede existente de instituições que oferecem EPTNM e a distribuição territorial dos cursos. [cite: 329]
4.  [cite_start]**Projetar** tendências futuras do mercado de trabalho para subsidiar o planejamento estratégico da expansão da EPTNM. [cite: 330]
5.  [cite_start]**Atender** integralmente às oito dimensões de dados exigidas pelo Edital nº 5/2025. [cite: 331]

## 3. Conformidade com o Edital Nº 5/2025

A plataforma foi concebida para atender plenamente aos critérios de avaliação e às dimensões de dados estipuladas no edital.

### Critérios de Avaliação (Item 5.4)

| Critério | Nível de Atendimento | Justificativa |
| :--- | :--- | :--- |
| **Clareza** | [cite_start]Nível 3 (Completo/Detalhado) [cite: 117] | [cite_start]A documentação, a arquitetura e a interface da plataforma são projetadas para serem claras, intuitivas e compreensíveis. [cite: 105] |
| **Justificativa** | [cite_start]Nível 3 (Completo/Detalhado) [cite: 117] | [cite_start]Todas as fontes de dados, tecnologias e modelos estatísticos são justificados com base em sua confiabilidade, relevância e adequação ao problema. [cite: 106] |
| **Detalhamento** | [cite_start]Nível 3 (Completo/Detalhado) [cite: 117] | [cite_start]O código-fonte será comentado, e a metodologia de ETL (Extração, Transformação e Carga) será documentada passo a passo para garantir a replicabilidade. [cite: 107] |
| **Fonte de Dados** | [cite_start]Nível 3 (Completo/Detalhado) [cite: 117] | [cite_start]Utilizamos exclusivamente fontes de dados públicas e reconhecidas por sua confiabilidade, como IBGE, MTE (CAGED/RAIS), MEC (SISTEC) e MDS (CadÚnico). [cite: 108, 335, 337, 339, 340] |
| **Impacto Potencial** | [cite_start]Nível 3 (Completo/Detalhado) [cite: 117] | [cite_start]A ferramenta gera evidências diretas para a formulação de políticas públicas, otimizando a alocação de recursos e aumentando a empregabilidade dos egressos. [cite: 110] |

### Dimensões de Dados Contempladas (Item 5.6)

A plataforma integra e analisa dados de todas as oito dimensões, organizadas nos seguintes módulos:

| Dimensão | Fontes de Dados Principais | Módulo da Plataforma |
| :--- | :--- | :--- |
| [cite_start]🗂️ **Dados Econômicos** [cite: 122] | [cite_start]Novo CAGED, RAIS, SINE [cite: 335, 336] | Módulo 1 (Vagas e Habilidades) e 4 (Projeção) |
| [cite_start]👥 **Dados Demográficos** [cite: 123] | [cite_start]IBGE (Censo, PNAD Contínua) [cite: 337] | Módulo 2 (Análise Sociodemográfica) |
| [cite_start]🎓 **Dados de Acompanhamento de Egressos** [cite: 124] | [cite_start]RAIS, SISTEC, Plataforma Nilo Peçanha [cite: 340, 341] | Módulo 3 (Oferta Educacional) |
| [cite_start]❤️ **Dados Sociais** [cite: 126] | [cite_start]CadÚnico, IBGE, Atlas da Vulnerabilidade (IPEA) [cite: 339, 387] | Módulo 2 (Análise Sociodemográfica) |
| [cite_start]🗣️ **Dados de Percepção/Opinião** [cite: 128] | [cite_start]CNI (Mapa do Trabalho Industrial) [cite: 342, 388] | Módulo 4 (Projeção de Mercado) |
| [cite_start]🏫 **Dados de Estrutura da Rede** [cite: 130] | [cite_start]Censo Escolar, Plataforma Nilo Peçanha [cite: 340] | Módulo 3 (Oferta Educacional) |
| [cite_start]⏳ **Dimensão Temporal** [cite: 131] | Séries históricas de todas as fontes | Todos os Módulos |
| [cite_start]🗺️ **Dimensão Geográfica** [cite: 132] | Dados com recorte municipal, estadual e regional | Todos os Módulos |

## 4. Arquitetura e Metodologia

A plataforma é construída sobre uma arquitetura de microsserviços, utilizando tecnologias de código aberto para garantir escalabilidade e manutenibilidade.

-   **Linguagem Principal:** Python
-   [cite_start]**Processamento de Dados (ETL):** Scripts de coleta via APIs públicas, downloads automáticos e web scraping supervisionado. [cite: 347]
-   [cite_start]**Banco de Dados:** PostgreSQL com a extensão PostGIS para suporte a dados geoespaciais. [cite: 350]
-   [cite_start]**Visualização e Dashboards:** Dash e Plotly para painéis interativos. [cite: 351]
-   [cite_start]**Modelagem e Projeção:** Bibliotecas como `scikit-learn`, `statsmodels` e `Prophet` para análise de séries temporais e projeções de demanda. [cite: 352]

O código será aberto e disponibilizado integralmente neste repositório, permitindo que qualquer estado ou instituição possa replicar ou adaptar a ferramenta.

## 5. Estrutura do Repositório

```
.
├── 📄 docs/                # Documentação do projeto (Proposta, Análise do Edital)
├── 📊 data/                # Scripts para aquisição e tratamento de dados
├── 📈 notebooks/           # Jupyter Notebooks para análise exploratória e modelagem
├── ⚙️ src/                  # Código-fonte da aplicação/plataforma
├── 📜 LICENSE              # Licença de uso do projeto
└── 📖 README.md            # Este arquivo
```

## 6. Como Executar o Protótipo (Instruções Futuras)

*(Esta seção será detalhada conforme o desenvolvimento do protótipo avança. Incluirá passos para configurar o ambiente, instalar dependências e executar a aplicação localmente).*

## 7. Licença

[cite_start]Este projeto é disponibilizado em conformidade com o item 1.8 do Edital. [cite: 16] O conteúdo pode ser utilizado e compartilhado para fins não comerciais, desde que o trabalho seja distribuído inalterado, na íntegra, e com o devido crédito aos autores (Universidade Federal de Uberlândia - UFU).

## 8. Contato e Responsáveis

-   **Vivian Consuelo Reolon Schmidt** - Orientadora
-   **Felipe Goulart Pereira** - Discente

---
