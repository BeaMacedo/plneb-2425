# TPC2 - Expressões Regulares

Nesta pasta, encontra-se o ficheiro `Ficha_RE_1.ipynb`, que implementa diversas funções relacionadas com expressões regulares. Seguidamente estão descritas as funcionalidades desenvolvidas, acompanhadas de exemplos de uso.

## 1.1 `correspondencia_i()`

**Descrição:** 
Verifica se a palavra "hello" aparece no início da linha.

**Exemplo:**
```python
Input: "hello world"
Output: True
```

## 1.2. `correspondencia()`

**Descrição:** 
Verifica se a palavra "hello" aparece em qualquer posição da linha.

**Exemplo:**
```python
Input: "hi, hello there"
Output: True
```

## 1.3. `correspondencias()`

**Descrição:** 
Encontra todas as ocorrências da palavra "hello" numa linha, independentemente  da palavra ser escrita com maiúsculas ou minúsculasdas.
**Exemplo:**
```python
Input: "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
Output: ['Hello', 'hello', 'hello', 'HELLO']
```

## 1.4. `replace()`

**Descrição:** 
Substitui todas as ocorrências da palavra "hello" por "*YEP*".

**Exemplo:**
```python
Input: "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
Output: *YEP* there! Uh, hi, *YEP*, it's me... Heyyy, *YEP*? *YEP*!
```

## 1.5. `split()`

**Descrição:** 
Separa uma string com base nas ocorrências do caracter vírgula.

**Exemplo:**
```python
Input: "bananas, laranjas, maçãs, uvas, melancias, cerejas, kiwis, etc."
Output: ['bananas', ' laranjas', ' maçãs', ' uvas', ' melancias', ' cerejas', ' kiwis', ' etc.']
```

## 2. `palavra_magica()`

**Descrição:** 
Verifica se uma frase termina com a expressão "por favor" seguido de um sinal válido de pontuação.

**Exemplo:**
```python
Input: "Posso ir à casa de banho, por favor?"
Output: True
```

## 3. `narcissismo()`

**Descrição:** 
Calcula quantas vezes a palavra "eu" aparece numa string, independentemente das maiúsculas e minúsculas.

**Exemplo:**
```python
Input: "Eu não sei se eu quero continuar a ser eu. Por outro lado, eu ser eu é uma parte importante de quem EU sou."
Output: 6
```

## 4. `troca_de_curso()`

**Descrição:** 
Substitui todas as ocorrências de "LEI" pelo nome de um curso fornecido.

**Exemplo:**
```python
Input: "LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei.","LEB"
Output: LEB é o melhor curso! Adoro LEB! Gostar de LEB devia ser uma lei.
```

## 5. `soma_string()`

**Descrição:** 
Recebe uma string com vários números separados por uma vírgula e devolve a soma destes números.

**Exemplo:**
```python
Input: "4,-6,2,3,8,-3,0,2,-5,1"
Output: 6
```

## 6. `pronomes()`

**Descrição:** 
Encontra e devolve todos os pronomes pessoais presentes numa frase.

**Exemplo:**
```python
Input: "Eu e tu sabemos que ela é mais inteligente que ele, mas nós nem sabemos sobre vós, e eles e elas estão confusos."
Output: ['Eu', 'tu', 'ela', 'ele', 'nós', 'vós', 'eles', 'elas']
```

## 7. `variavel_valida()`

**Descrição:** 
Verifica se uma string é um nome válido para uma variável (começa por uma letra e contém apenas letras, números ou underscores).

**Exemplo:**
```python
Input: "variavel1"
Output: True

Input: "Espaço Aqui"
Output: False
```

## 8. `inteiros()`

**Descrição:** 
Devolve todos os números inteiros (positivos e negativos) presentes numa string.

**Exemplo:**
```python
Input: "O João tem 25 anos, a Maria tem -7 e a soma das idades é 18."
Output: ['25', '-7', '18']
```

## 9. `underscores()`

**Descrição:** 
Substitui todos os espaços numa string por underscores e se aparecerem vários espaços seguidos, são substituídos por apenas um underscore.

**Exemplo:**
```python
Input: "Teste teste    tes  te"
Output: Teste_teste_tes_te
```

## 10. `codigos_postais()`

**Descrição:** 
Divide uma lista de códigos postais no formato "XXXX-XXX" com base no hífen em pares de strings.

**Exemplo:**
```python
Input: ['4700-000', '1234-567']
Output: [('4700', '000'), ('1234', '567')]
```

---

