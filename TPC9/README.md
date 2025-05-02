# TPC9 - Análise de Word Embeddings no Universo Harry Potter
Neste TPC são exploradas as relações semânticas entre palavras no universo de Harry Potter utilizando o modelo Word2Vec. O objetivo foi analisar como o modelo captura as conexões entre personagens, objetos mágicos e conceitos fundamentais da narrativa.
O TPC foi desenvolvido em Python utilizando Gensim para implementação do Word2Vec e dois livros da série ("Harry Potter e a Pedra Filosofal" e "Harry Potter e a Câmara Secreta") como corpus.

## Análises realizadas
### model.wv.most_similar("magia")
output:
```python
[('escola', 0.8521685004234314),
 ('sonserina', 0.8346917033195496),
 ('usar', 0.8305774927139282),
 ('escondido', 0.8069193959236145),
 ('seção', 0.7950572967529297),
 ('ministro', 0.765231728553772),
 ('casa', 0.7650980949401855),
 ('quadribol', 0.7621254324913025),
 ('reservada', 0.7567346096038818),
 ('taça', 0.7554255723953247)]
```
Os resultados obtidos com este comando fazem sentido dentro do contexto. As palavras mais similares, como "escola", "sonserina", "usar", "quadribol" e "ministro", estão todas fortemente ligadas à prática e ao conceito de magia na narrativa. Por exemplo, Hogwarts, onde os bruxos aprendem magia, e elementos como sonserina e quadribol são representações diretas da magia no mundo bruxo. O modelo conseguiu destacar a relação estreita entre "magia" e outros termos fundamentais do universo mágico. Essas palavras refletem aspetos como a aprendizagem de magia, a aplicação da magia e a estrutura do mundo bruxo, demonstrando que o modelo entendeu bem as conexões semânticas relevantes.


### model.wv.most_similar("varinha")
output:
```python
[('mão', 0.8651896715164185),
 ('boca', 0.8623641729354858),
 ('vassoura', 0.8011002540588379),
 ('raiva', 0.7804672122001648),
 ('cabeça', 0.7672806978225708),
 ('nuca', 0.7514667510986328),
 ('testa', 0.7420324683189392),
 ('visão', 0.7399470210075378),
 ('cara', 0.7350703477859497),
 ('capa', 0.7331789135932922)]
```
Os resultados obtidos para a palavra "varinha" no modelo fazem sentido dentro do contexto do universo mágico de Harry Potter. Palavras como "mão", "boca", e "vassoura" estão diretamente relacionadas à utilização da varinha e a objetos mágicos com os quais ela é associada. A "mão" é onde a varinha é segurada, a "boca" é usada para proferir feitiços, e a "vassoura" está ligada ao mundo mágico em que a varinha é um dos principais instrumentos. Outras palavras, como "raiva" e "cabeça", refletem o contexto emocional e físico em que a varinha é utilizada, como feitiços lançados em momentos de raiva ou gestos com o corpo.

### model.wv.most_similar(positive=["draco", "grifinória"], negative=["harry"])
output:
```python
[('lufa', 0.6450467705726624),
 ('sonserina', 0.6298632621765137),
 ('corvinal', 0.6073724031448364),
 ('pontos', 0.5893895626068115),
 ('magia', 0.5710559487342834),
 ('sair', 0.5691394209861755),
 ('capitão', 0.565392017364502),
 ('membro', 0.5632210373878479),
 ('posse', 0.5358288288116455),
 ('torre', 0.5316007733345032)]
```
Este comando procura palavras associadas à rivalidade entre as casas de Draco Malfoy (Sonserina) e Grifinória, sem considerar Harry Potter. Os resultados incluem palavras como "lufa" (Lufa-Lufa), "sonserina" e "corvinal", que refletem a competição entre as casas de Hogwarts. Também aparecem termos como "pontos" (relacionados ao sistema de pontos das casas) e "capitão" (em referência a cargos importantes nas competições, como o quadribol). Esses resultados destacam a dinâmica escolar e as interações competitivas entre os estudantes, sem focar diretamente em Harry.


### model.wv.similarity('voldemort','perigo')
output:
```python
similaridade entre voldemort e perigo: 0.6801784038543701
```
A similaridade de 0.68 entre "Voldemort" e "perigo" faz sentido, pois reflete a forte relação semântica entre esses dois conceitos, revelando que o modelo capturou a essência de Voldemort como a personificação do perigo no universo. Voldemort, um bruxo extremamente poderoso e temido, está intrinsicamente ligado ao conceito de perigo, já que é a principal ameaça para muitas personagens. Embora "Voldemort" seja uma figura específica e "perigo" um conceito mais amplo, ambos compartilham um contexto de ameaça e risco, o que gera uma relação significativa entre as palavras, explicando a similaridade observada.


### model.wv.most_similar(positive=["hogwarts", "professor"], negative=["escola"])
output:
```python
[('tom', 0.6563527584075928),
 ('alvo', 0.6521009802818298),
 ('gringotes', 0.6315924525260925),
 ('engraçado', 0.6292930245399475),
 ('problema', 0.6085200309753418),
 ('diretor', 0.6060552597045898),
 ('famoso', 0.5943508744239807),
 ('nome', 0.5844963788986206),
 ('único', 0.5829630494117737),
 ('ai', 0.5819411277770996)]
```
Esta analogia tem como objetivo identificar o que há de específico num professor de Hogwarts, excluindo a noção genérica de escola. Os primeiros resultados fazem sentido dentro do universo de Harry Potter: surgem nomes como "tom" (Tom Riddle) e "alvo" (Alvo Dumbledore), ambos personagens ligadas à escola e ao ensino. Também aparecem termos como "diretor", "famoso" e "único", que capturam o prestígio e a singularidade da instituição. No entanto, a partir de certo ponto, começam a surgir palavras menos relevantes como "engraçado", "problema" ou "ai", provavelmente vêm de diálogos onde os professores usam essas expressões.


### model.wv.most_similar(positive=["hogwarts", "professor"], negative=["aluno"])
output:
```python
[('rúbeo', 0.6316468715667725),
 ('dumbledore', 0.6284853219985962),
 ('mim', 0.6197583079338074),
 ('quem', 0.6038243174552917),
 ('sim', 0.5754674077033997),
 ('papai', 0.5699341893196106),
 ('senhor', 0.5652090311050415),
 ('tom', 0.5648303627967834),
 ('morrer', 0.5603104829788208),
 ('ah', 0.5518695712089539)]
```
Esta analogia mostra que o modelo capturou dinâmicas educacionais do universo Harry Potter. Figuras como Hagrid ("Rúbeo") e Dumbledore emergiram como representações típicas da autoridade docente, enquanto termos como "morrer" refletem eventos trágicos marcantes envolvendo professores. A aparição ocasional de palavras como "papai" pode indicar tanto ruído quanto referências a relações familiares entre gerações de bruxos.

