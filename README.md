# Plataforma Integrada para Mapeamento da Demanda por Educação Profissional Técnica de Nível Médio

**Proponente:** Universidade Federal de Uberlândia (UFU) \
**Edital de Referência:** Edital Nº 5/2025 - MEC/SETEC \
**Status do Projeto:** Em desenvolvimento (Fase de Prototipagem)

## 1. Sobre o Projeto

Este repositório apresenta o protótipo da Plataforma Integrada para o Mapeamento da Demanda por Educação Profissional Técnica de Nível Médio (EPTNM). O projeto foi desenvolvido em resposta à Chamada Pública do Ministério da Educação (MEC), por intermédio da Secretaria de Educação Profissional e Tecnológica (Setec), como uma ferramenta de apoio à implementação do Programa Juros por Educação.

O objetivo da plataforma é fornecer um instrumento de código aberto, robusto e replicável, capaz de auxiliar gestores públicos e instituições de ensino a planejar a oferta de cursos técnicos. A análise busca alinhar a formação profissional às necessidades reais do mercado de trabalho e aos arranjos produtivos locais e regionais, a partir da consolidação e integração de dados de fontes governamentais abertas.

## 2. Objetivos da Plataforma

#### Objetivo Geral
Desenvolver uma plataforma digital aberta e interoperável para mapear a demanda por cursos técnicos de nível médio, através do cruzamento de dados sobre mercado de trabalho, perfil populacional e oferta educacional.

#### Objetivos Específicos
1. Identificar ocupações em crescimento e setores produtivos com maior demanda por qualificação técnica.
2. Mapear características sociodemográficas, educacionais e de vulnerabilidade social da população jovem.
3. Diagnosticar a rede existente de instituições que oferecem EPTNM e a distribuição territorial dos cursos.
4. Projetar tendências futuras do mercado de trabalho para subsidiar o planejamento estratégico da expansão da EPTNM.
5. Atender integralmente às oito dimensões de dados exigidas pelo Edital nº 5/2025.

## 3. Conformidade com o Edital Nº 5/2025

A plataforma foi desenvolvida para atender aos critérios de avaliação e às dimensões de dados estipuladas no edital.

#### Critérios de Avaliação (Item 5.4)

| Critério | Nível de Atendimento | Justificativa |
| :--- | :--- | :--- |
| **Clareza** | Nível 3 (Completo/Detalhado) | A documentação, a arquitetura e a interface da plataforma são projetadas para serem claras, intuitivas e compreensíveis. |
| **Justificativa** | Nível 3 (Completo/Detalhado) | Todas as fontes de dados, tecnologias e modelos estatísticos são justificados com base em sua confiabilidade, relevância e adequação ao problema. |
| **Detalhamento** | Nível 3 (Completo/Detalhado) | O código-fonte será comentado, e a metodologia de ETL (Extração, Transformação e Carga) será documentada para garantir a replicabilidade. |
| **Fonte de Dados** | Nível 3 (Completo/Detalhado) | Utiliza exclusivamente fontes de dados públicas e reconhecidas, como IBGE, MTE (CAGED/RAIS), MEC (SISTEC) e MDS (CadÚnico). |
| **Impacto Potencial** | Nível 3 (Completo/Detalhado) | A ferramenta gera evidências para a formulação de políticas públicas, otimizando a alocação de recursos e aumentando a empregabilidade dos egressos. |

#### Dimensões de Dados Contempladas (Item 5.6)

A plataforma integra e analisa dados de todas as dimensões solicitadas, organizadas nos seguintes módulos:

| Dimensão | Fontes de Dados Principais | Módulo da Plataforma |
| :--- | :--- | :--- |
| **Dados Econômicos** | Novo CAGED, RAIS, SINE | Módulo 1 (Vagas e Habilidades) e 4 (Projeção) |
| **Dados Demográficos** | IBGE (Censo, PNAD Contínua) | Módulo 2 (Análise Sociodemográfica) |
| **Dados de Acompanhamento de Egressos** | RAIS, SISTEC, Plataforma Nilo Peçanha | Módulo 3 (Oferta Educacional) |
| **Dados Sociais** | CadÚnico, IBGE, Atlas da Vulnerabilidade (IPEA) | Módulo 2 (Análise Sociodemográfica) |
| **Dados de Percepção/Opinião** | CNI (Mapa do Trabalho Industrial) | Módulo 4 (Projeção de Mercado) |
| **Dados de Estrutura da Rede** | Censo Escolar, Plataforma Nilo Peçanha | Módulo 3 (Oferta Educacional) |
| **Dimensão Temporal** | Séries históricas de todas as fontes | Todos os Módulos |
| **Dimensão Geográfica** | Dados com recorte municipal, estadual e regional | Todos os Módulos |

## 4. Arquitetura e Metodologia

A plataforma é construída sobre uma arquitetura de microsserviços, utilizando tecnologias de código aberto para garantir escalabilidade e manutenibilidade.

- **Linguagem Principal:** Python
- **Processamento de Dados (ETL):** Scripts de coleta via APIs públicas, downloads automáticos e web scraping supervisionado.
- **Banco de Dados:** PostgreSQL com a extensão PostGIS para suporte a dados geoespaciais.
- **Visualização e Dashboards:** Dash e Plotly para painéis interativos.
- **Modelagem e Projeção:** Bibliotecas como `scikit-learn`, `statsmodels` e `Prophet` para análise de séries temporais e projeções de demanda.

## 5. Estrutura do Repositório

O projeto está organizado da seguinte forma:

- **docs/**: Contém a documentação de apoio do projeto, como a Proposta inicial e a análise do Edital.
- **data/**: Inclui os scripts para aquisição, limpeza e tratamento dos dados de fontes públicas.
- **notebooks/**: Armazena os Jupyter Notebooks utilizados para a análise exploratória dos dados e desenvolvimento dos modelos.
- **src/**: Contém o código-fonte principal da aplicação da plataforma.
- **LICENSE**: Arquivo com a licença de uso do projeto.
- **README.md**: Documento de apresentação do repositório (este arquivo).

## 6. Como Executar o Protótipo

Esta seção será detalhada conforme o desenvolvimento do protótipo avança. Incluirá os passos para configuração do ambiente, instalação de dependências e execução da aplicação localmente.

## 7. Licença

Este projeto é disponibilizado em conformidade com o item 1.8 do Edital. O conteúdo pode ser utilizado e compartilhado para fins não comerciais, desde que o trabalho seja distribuído inalterado, na íntegra, e com o devido crédito aos autores (Universidade Federal de Uberlândia - UFU).

## 8. Contato e Responsáveis

- Vivian Consuelo Reolon Schmidt - Docente e Orientadora
- Felipe Goulart Pereira - Discente e Desenvolvedor
