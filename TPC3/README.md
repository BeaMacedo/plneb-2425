# TPC3

Nesta pasta, encontra-se o ficheiro 'TPC3.py', que processa um dicionário de conceitos médicos e gera um arquivo HTML com a formatação dos conceitos e suas descrições. 
Seguidamente, são identificados todas as etapas realizadas:

## 1. Leitura do Arquivo:
O documento 'dicionario_medico.txt' é aberto e o conteúdo é lido.

## 2. Processamento do Texto:

### 2.1. São removidas as quebras de página (\f). 

```python
texto = re.sub("\f","",texto)
```

### 2.2. É adicionado um ponto final à palavra “Significado”. 
Como a palavra "Significado" aparece no início do texto, uma única vez, é adicionado um ponto final no fim da mesma. Isto é necessário para garantir que o primeiro conceito  Å seja bem identificado, tendo em conta a lógica implementada em seguida.

```python
texto = re.sub(r"Significado","Significado.",texto)
```

### 2.3. É inserido o marcador ‘@’ após as descrições de conceitos.
As descrições dos conceitos no texto terminam com um ponto final seguido por duas quebras de linha (\n\n). Como sabemos que os conceitos começam logo após este ponto final, o marcador ‘@’ é inserido após cada ponto final seguido de duas quebras de linha e será este marcador que vai ajudar a identificar o início de cada novo conceito no texto, facilitando a extração dos dados.

```python
texto = re.sub(r"\.\n\n",".\n\n@",texto)
```

### 2.4. Remoção do marcador ‘@’ quando este é inserido no início de uma frase que começa por letra maiuscula e termina com ponto final
Se o ‘conceito’ começa com uma letra maiuscula e termina com um ponto final, este não deverá ser um conceito, mas pode ser uma frase da descrição de algum conceito e, por isso, o marcador ‘@’ não deve estar presente. Por exemplo, o conceito "quimiotaxia" é um exemplo de um conceito que apresenta duas fases de descrição e existe uma quebra de página entre as frases, pelo que é necessário remover o marcador da segunda frase, que estava a ser identificada como um conceito.

```python
texto = re.sub(r"@([A-Z][^@]*\.)", r"\1", texto)
```

## 3. Extração dos conceitos e as respetivas descrições.
Com a expressão regular r'@(.*)\n([^@]*)', é extraído o conceito e a descrição. O marcador ‘@’ marca o início de um conceito, e a expressão procura tudo o que vem após o marcador até uma quebra de linha (\n) e captura a descrição até o próximo marcador ‘@’.

```python
conceitos_raw = re.findall(r'@(.*)\n([^@]*)', texto)
```

## 4. Armazenar os conceitos e suas descrições em uma lista estruturada.
Utilizando a função ‘limpa_descricao’ é realizada a limpeza das descrições e são armazenados os conceitos e as descrições de forma estruturada numa lista de tuplos, o que facilita a geração do HTML posteriormente, já que cada tuplo contém um conceito e a sua descrição correspondente.

```python
conceitos = [(designacao, limpa_descricao(descricao)) for designacao, descricao in conceitos_raw]
```

## 5. Geração do HTML para apresentar os conceitos
A função ‘gera_html’ cria a estrutura HTML para exibir os conceitos e suas descrições, cujo resultado é gravado no arquivo ‘dicionario_medico.html’, que pode ser aberto no navegador. Isso permite visualizar o dicionário de conceitos médicos de forma interativa.
