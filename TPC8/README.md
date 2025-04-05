# TPC8

Este script realiza a extração automatizada de dados clínicos do site Atlas da Saúde, navegando por categorias de doenças organizadas alfabeticamente. A informação é recolhida de forma estruturada e exportada em formato JSON.


## Funções implementadas
### adquirir_letras()

Inicializa o processo de scraping ao identificar e iterar sobre todos os grupos de doenças categorizadas por letra. Para cada grupo (ex: A, B, C...), encaminha a letra correspondente para a função extrair_desc_desig.

#### Funcionamento:

- Analisa os elementos com a classe views-summary views-summary-unformatted, os quais representam os filtros por letra disponíveis na página principal.

- Para cada um desses elementos, extrai o valor textual da letra e converte para minúsculas.

- Utiliza a função extrair_desc_desig(letra) para processar as doenças correspondentes.

### doenca_info(url)

Responsável por extrair o conteúdo detalhado de uma página específica de uma doença. Essa informação é organizada em múltiplos campos clínicos e estruturais para facilitar a análise semântica posterior.

#### Campos extraídos:
- InformaçãoInicial: Texto introdutório antes da primeira secção marcada por (`<h2>`).
- Causas: Causas descritas em parágrafos e/ou listas.
- Sintomas: Divididos em duas partes — um bloco de texto e uma lista estruturada.
- Diagnóstico: Descrição dos métodos diagnósticos ou critérios clínicos.
- Tratamento: Orientações terapêuticas ou procedimentos sugeridos.
- ArtigosRelacionados: Lista de links e títulos de conteúdos relacionados.
- Site: Links externos mencionados na ficha da doença.
- Nota: Informações complementares fornecidas pela fonte.
- Fonte: Origem editorial ou científica da informação exibida.

#### Funcionamento:

1. Realiza uma requisição HTTP à página da doença.
2. Identifica o bloco div.node-doencas, contendo o conteúdo principal.
3. Antes da aparição do primeiro (`<h2>`), recolhe o texto introdutório.
4. A seguir, percorre cada (`<h2>`) e recolhe os elementos subsequentes até o próximo cabeçalho para classificar o conteúdo nas secções clínicas.
5. Extrai também metainformações adicionais (nota, site, fonte) que estão fora do corpo principal.


### extrair_desc_desig(letter)

Dada uma letra, percorre todas as doenças que iniciam com a letra em questão e recolhe tanto os dados de listagem como os dados completos através da função doenca_info(url).

#### Dados processados por doença:
- Designação: Nome da doença.
- Resumo: Descrição breve apresentada na listagem.
- URL: Link completo para a página de detalhes.
- Conteúdo clínico detalhado: Obtido via chamada a doenca_info(url).

#### Funcionamento:
1. Constrói a URL da página específica da letra.
2. Realiza a requisição e faz parsing do HTML.
3. Identifica todos os blocos div.views-row que representam doenças listadas.
4. Para cada bloco:
      - Extrai o nome da doença e a sua descrição resumida.
      - Gera a URL completa de acesso à página da doença.
      - Invoca a função doenca_info(url) e armazena todos os dados extraídos no dicionário 
        global doencas.

## Estrutura e Armazenamento dos Dados

O dicionário doencas, construído progressivamente ao longo da execução, utiliza como chave o nome da doença e como valor um dicionário contendo todas as informações recolhidas.

Exemplo da estrutura final no ficheiro doencas.json:

```python
    "Wilms, Tumor de": {
        "Resumo": "O tumor de Wilms (nefroblastoma) é um cancro nos rins que pode aparecer no feto e ser assintomático durante anos após o nascimento. Normalmente, manifesta-se em menores de 5 anos, embora de vez em quando apareça em crianças mais velhas e raramente em adultos.",
        "URL": "https://www.atlasdasaude.pt//content/wilms-tumor-de",
        "InformaçãoInicial": "O tumor de Wilms (nefroblastoma) é um cancro nos rins que pode aparecer no feto e ser assintomático durante anos após o nascimento. Normalmente, manifesta-se em menores de 5 anos, embora de vez em quando apareça em crianças mais velhas e raramente em adultos.A causa do tumor de Wilms é desconhecida, embora em alguns casos possa ter a sua origem numa anomalia genética. As crianças com determinadas deficiências de nascimento, como ausência de íris ou crescimento excessivo de um lado do corpo, cuja causa pode ser uma anomalia genética, correm mais riscos de desenvolver um tumor de Wilms. Os sintomas incluem dilatação abdominal (por exemplo, a rápida necessidade de alterar o tamanho da fralda), dor abdominal, febre, falta de apetite, náuseas e vómitos. Há sangue na urina entre 15 e 20 por cento dos casos e pode haver elevação da tensão arterial. Este cancro pode estender-se a outras partes do corpo, sobretudo aos pulmões, provocando tosse e sufoco.Normalmente, pode-se palpar um volume (massa) no abdómen da criança. O prognóstico depende da aparência microscópica do tumor, da sua extensão no momento do diagnóstico e da idade da criança.",
        "Causas": "",
        "Sintomas": [
            "",
            []
        ],
        "Diagnóstico": "",
        "Tratamento": "",
        "ArtigosRelacionados": {},
        "Site": "http://www.manualmerck.net",
        "Nota": "As informações e conselhos disponibilizados no Atlas da Saúde de A-Z não substituem o parecer/opinião do seu Médico e/ou Farmacêutico.",
        "Fonte": ""
    },
    "Wilson, Doença de": {
        "Resumo": "A doença de Wilson deve o seu nome a Samuel Wilson que, pela primeira vez, a descreveu, em 1912, como \"degenerescência lenticular progressiva\": uma doença neurológica familiar e letal, acompanhada de doença hepática crónica que conduz à cirrose.",
        "URL": "https://www.atlasdasaude.pt//content/wilson-doenca-de",
        "InformaçãoInicial": "A doença de Wilson deve o seu nome a Samuel Wilson que, pela primeira vez, a descreveu, em 1912, como \"degenerescência lenticular progressiva\": uma doença neurológica familiar e letal, acompanhada de doença hepática crónica que conduz à cirrose. É, também, denominada como degenerescência hepatolenticular.Trata-se de uma doença rara, afectando 1 em 30.000 a 100.000 indivíduos, hereditária, de transmissão autossómica recessiva, associada a perturbação do metabolismo do cobre, que resulta do defeito na excreção deste metal pela bile, levando à sua acumulação, inicialmente, no hepatócito e, posteriormente, em diversos órgãos e tecidos, particularmente, cérebro, córnea e rins.As manifestações clínicas da doença, relacionadas sobretudo com o fígado e sistema nervoso central, são extremamente variáveis. As lesões hepáticas precedem, em cerca de 10 anos, a doença neurológica, ocorrendo em geral o seu diagnóstico na infância ou adolescência. O seu espectro vai desde simples elevação das transaminases (assintomática) até cirrose e falência hepática fulminante. As manifestações clínicas neurológicas podem, em alguns casos, ser a forma de apresentação da doença, mais frequentemente na 3ª década de vida.Se não tratada a doença acarreta grande morbilidade e morte, inexorável e precoce. Se diagnosticada e tratada precocemente, é possível prevenir ou reverter algumas das manifestações da doença. As estratégias disponíveis para o tratamento consistem na redução da absorção do cobre, a promoção da sua eliminação e, em casos extremos, a transplantação hepática. A dieta com restrição de alimentos ricos em cobre não é suficiente para causar o balanço negativo daquele metal no organismo. Mesmo assim, devem ser evitados, entre outros, marisco, fígado, chocolate, cogumelos, nozes, avelãs e castanhas.",
        "Causas": "",
        "Sintomas": [
            "",
            []
        ],
        "Diagnóstico": "",
        "Tratamento": "",
        "ArtigosRelacionados": {},
        "Site": "http://www.linharara.pt",
        "Nota": "As informações e conselhos disponibilizados no Atlas da Saúde de A-Z não substituem o parecer/opinião do seu Médico e/ou Farmacêutico.",
        "Fonte": ""
    },
```

