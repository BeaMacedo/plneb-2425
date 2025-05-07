# TPC10 - Web Scraper para a Revista Medicina Interna (RPMI)

Neste TPC foi desenvolvido um script Python que extrai informações de artigos científicos da Revista Portuguesa de Medicina Interna usando Beautiful Soup.

## Seletor html utilizado

```python
<h3 class="title">
  <a id="article-XXXX" href="URL_DO_ARTIGO">...</a>
</h3>
```

1. Acede à página principal da edição
2. Encontra todos os elementos <h3> com classe title
3. Extrai o link do elemento <a> interno

## Extração das informações de cada artigo

### Título

```python
<h1 class="page_title">TÍTULO DO ARTIGO</h1>
```
1. Procura pela tag <h1> com classe page_title
2. Remove espaços extras com strip()

### Abstract

```python
<section class="item abstract">
  <h2>Abstract</h2>
  <p>Texto do abstract...</p>
</section>
```
1. Localiza a seção com classe item abstract
2. Concatena todos os parágrafos <p> internos
3. Remove quebras de linha e espaços múltiplos

### DOI

```python
<section class="item doi">
  <a href="LINK_DOI">...</a>
</section>
```

1. Encontra a seção com classe item doi
2. Extrai o link do elemento <a> filho

### Data de Publicação

```python
<div class="item published">
  <section>
    <div class="value">
      <span>AAAA-MM-DD</span>
    </div>
  </section>
</div>
```

1. Localiza a div com classe item published
2. Extrai o texto do elemento <span> interno

### Palavras-Chave

```python
<meta name="citation_keywords" content="PALAVRA-CHAVE">
```

1. Coleta todos os meta tags com name="citation_keywords"
2. Extrai o conteúdo do atributo content

## Ficheiro json resultante

Exemplo da estrutura:

```python
    {
        "title": "Significado Clínico da Elevação Extrema da Velocidade de Sedimentação: Diagnósticos e Sobrevida em 681 Doentes num Hospital Português",
        "abstract": "Introdução: O nosso objetivo foi estudar a associação entre elevações extremas da velocidade de sedimentação (VS) (>100 mm/h) e a distribuição por categorias de doenças, doenças, idade, sexo, níveis de proteína C-reactiva e sobrevida a 5 anos. Métodos: Estudo retrospetivo de todos os doentes com elevação extrema da VS avaliados num hospital português de 1 de Janeiro de 2008 a 31 de Dezembro de 2012. Variáveis independentes incluíram categorias de doenças, subcategorias, idade, sexo e níveis de PCR. A situação vital e data de morte foram determinadas pelo uso do Sistema de Prescrição Eléctrica português. Resultados: Uma VS superior a 100 mm/h foi determinada em 681 doentes (1,5% de todas as avaliações de VS). A categoria diagnóstica mais frequente foi infecção (461, 65,1%), seguida de neoplasia (107, 15,1%), e de inflamação/ autoimunidade (85, 12,0%). A doença mais prevalente foi a pneumonia (227, 33,3% de todos os doentes). A infeção era menos provável nos doentes de ambulatório (20,7%), assim como a neoplasia em mulheres (11,4%). A mortalidade a cinco anos foi de 70,3%, superior nos doentes com neoplasia (83%) e inferior nos doentes com inflamação/autoimunidade (45,9%). Conclusão: Verificámos que quase todos os doentes com elevação extrema da VS têm uma etiologia identificável, com infecção a ser a causa em cerca de dois terços e a pneumonia a ser responsável em cerca de um terço de todos os doentes. A infecção foi menos provável em doentes de ambulatório, assim como a neoplasia em mulheres. Os níveis de VS e de PCR têm fraca correlação nestes doentes. A mortalidade a cinco anos foi de 70,3%, com a sobrevida a ser significativamente menor em doentes com neoplasia, e superior em doentes com inflamação/autoimunidade. Estes resultados poderão auxiliar à avaliação diagnóstica e prognóstica dos doentes com elevações extremas da VS.",
        "doi": "https://doi.org/10.24950/rspmi.2579",
        "publish_date": "2025-03-31",
        "keywords": [
            "Mortalidade",
            "Velocidade de Sedimentação"
        ]
    },
```
