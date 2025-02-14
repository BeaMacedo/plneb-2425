# TPC1 

Nesta pasta, encontra-se o ficheiro TPC1.py, que implementa várias funções que envolvem a manipulação de strings. Seguidamente, apresenta-se as funcionalidades desenvolvidas, assim como com exemplos de uso.

## 1. `reverse()`
**Descrição:**  
Esta função recebe uma string e retorna a string invertida.

- **Exemplo:**  
  **Input:** `"Bea"`  
  **Output:** `"aeB"`

---

## 2. `count_Aa()`
**Descrição:**  
Conta quantas vezes os caracteres "a" e "A" aparecem numa string.

- **Exemplo:**  
  **Input:** `"Ananas"`  
  **Output:** `a: 2, A: 1`

---

## 3. `count_Vowels()`
**Descrição:**  
Conta o número total de vogais presentes numa string.

- **Exemplo:**  
  **Input:** `"Luisao"`  
  **Output:** `4`

---

## 4. `str_Lowercase()`
**Descrição:**  
Converte todas as letras de uma string para minúsculas.

- **Exemplo:**  
  **Input:** `"ANA Beatriz"`  
  **Output:** `"ana beatriz"`

---

## 5. `str_Uppercase()`
**Descrição:**  
Converte todas as letras de uma string para maiúsculas.

- **Exemplo:**  
  **Input:** `"Ana Beatriz"`  
  **Output:** `"ANA BEATRIZ"`

---

## 6. `isCapicua()`
**Descrição:**  
Verifica se a string fornecida como argumento é capicua, ou seja, se é igual a si mesma quando invertida.

- **Exemplo:**  
  **Input:** `"Ana"`  
  **Output:** `True`

- **Exemplo:**  
  **Input:** `"Hello"`  
  **Output:** `False`
---

## 7. `isBalance()`
**Descrição:**  
Verifica se 2 strings estão balanceadas, ou seja se se todos os caracteres de uma string estão presentes na outra.

- **Exemplo:**  
  **Input:** `"banana", "ana"`  
  **Output:** `False`

  **Input:** `"ana", "banana"`  
  **Output:** `True`

  **Input:** `"ana", "nadar"`  
  **Output:** `True`

---

## 8. `count_occurences()`
**Descrição:**  
Conta o número de vezes que uma string aparece dentro de outra string.

- **Exemplo:**  
  **Input:** `"lo", "loLOLo"`  
  **Output:** `3`

---

## 9. `isAnagrama()`
**Descrição:**  
Verifica se duas strings são anagramas.

- **Exemplo:**  
  **Input:** `"hello", "world"`  
  **Output:** `False`

  **Input:** `"listen", "silent"`  
  **Output:** `True`
---

## 10. `ClassesAnag()`
**Descrição:**  
Dada uma lista com strings agrupa palavras que são anagramas na mesma classe, retornando um dicionário em que as chaves são as palavras ordenadas alfabeticamente e os valores são listas de palavras que são anagramas entre si.

- **Exemplo:**  
  **Input:** `["roma", "amor", "mora", "rat", "tar", "art", "boca", "cabo"]`  
  **Output:**  
  ```python
  {'amor': ['roma', 'amor', 'mora'],
   'art': ['rat', 'tar', 'art'],
   'abco': ['boca', 'cabo']}

