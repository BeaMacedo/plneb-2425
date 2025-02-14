#TPC1 - Create a function that:


#1 - given a string "s", reverse it.

def reverse(string):
    strInversa = string[::-1]
    return strInversa

s1 = "Bea"
print(f'Ex1: A string "{s1}" invertida fica: {reverse(s1)}')

#2 - given a string "s", returns how many "a" and "A" characters are present in it.
def count_Aa(string):
    num_A = string.count("A")
    num_a = string.count("a")
    return (num_A,num_a)

s2 = "Ananas"
print(f'Ex2: Existem {count_Aa(s2)[0]} "A" e {count_Aa(s2)[1]} "a" na string "{s2}"')

#3 - given a string "s", returns the number of vowels there are present in it.

def count_Vowels(string):
    contador = 0
    vogais = ["a","e","i","o","u"]
    s = string.lower()
    for i in s:
        if i in vogais:
            contador = contador + 1

    return contador

s3 = "Luisao"
print(f'Ex3: O numero de vogais na string "{s3}" é {count_Vowels(s3)}')

#4 - given a string "s", convert it into lowercase.
def str_Lowercase(string):
    return string.lower()

s4 = "ANA Beatriz"
print(f'Ex4: String "{s4}" em minusculas: {str_Lowercase(s4)}')

#5 - given a string "s", convert it into uppercase.

def str_Uppercase(string):
    return string.upper()

s5 = "Ana Beatriz"
print(f'Ex5: String "{s5}" em maiusculas: {str_Uppercase(s5)}')

#6 - Verifica se uma string é capicua.

def isCapicua(string):
    res = False
    if string.lower() == reverse(string.lower()):
        res = True
    return res

s6_1 = "Ana"
s6_2= "Hello"
print(f'Ex6: String "{s6_1}" é capicua - {isCapicua(s6_1)}')
print(f'Ex6: String "{s6_2}" é capicua - {isCapicua(s6_2)}')

#7 - Verifica se duas strings estão balanceadas (Duas strings, s1 e s2, estão balanceadas se todos os caracteres de s1 estão presentes em s2).

def isBalance(string1, string2):
    res = True
    s1 = str_Lowercase(string1)
    s2 = str_Lowercase(string2)
    for i in s1:
        if i not in s2:
            res = False
    
    return res

s7_1 = "banana"
s7_2 = "ana"

s7_3 = "ana"
s7_4 = "banana"

s7_5 = "ana"
s7_6 = "nadar"

print(f'Ex7: As strings s1: "{s7_1}" e s2: "{s7_2}" estao balanceadas - {isBalance(s7_1,s7_2)}')
print(f'Ex7: As strings s1: "{s7_3}" e s2: "{s7_4}" estao balanceadas - {isBalance(s7_3,s7_4)}')
print(f'Ex7: As strings s1: "{s7_5}" e s2: "{s7_6}" estao balanceadas - {isBalance(s7_5,s7_6)}')


#8 - Calcula o número de ocorrências de s1 em s2.

def count_occurences(string1, string2):
    s1 = str_Lowercase(string1)
    s2 = str_Lowercase(string2)
    return s2.count(s1)

s8_1 = "lo"
s8_2 = "loLOLo"
print(f'Ex8: O numero de ocorencias de s1: "{s8_1}" em s2: "{s8_2}" é {count_occurences(s8_1,s8_2)}')


#9 - Verifica se s1 é anagrama de s2

def isAnagrama(string1,string2):
    s1 = str_Lowercase(string1)
    s2 = str_Lowercase(string2)
    return sorted(s1) == sorted(s2)

s9_1 = "hello"
s9_2 = "world"

s9_3 = "listen"
s9_4 = "silent"

print(f'Ex9: A string s1: "{s9_1}" é anagrama de s2: "{s9_2}" - {isAnagrama(s9_1,s9_2)}')
print(f'Ex9: A string s1: "{s9_3}" é anagrama de s2: "{s9_4}" - {isAnagrama(s9_3,s9_4)}')



#10 - Dado um dicionário, calcular a tabela das classes de anagramas.

def ClassesAnag(lista):
    dictAnagram = {}
    for string in lista:
        palavra_ord = "".join(sorted(string))
        if palavra_ord in dictAnagram:
            dictAnagram[palavra_ord].append(string)
        else:
            dictAnagram[palavra_ord] = [string]
    return dictAnagram

l = ["roma", "amor", "mora", "rat", "tar", "art", "boca", "cabo"]

print(f'Ex10: As classes de anagrama da lista {l} são: {ClassesAnag(l)}')