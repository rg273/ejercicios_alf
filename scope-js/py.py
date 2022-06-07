from itertools import count


Vocales = ["a","e","i","o","u"]
def excludes_vowel_counter(string):
    contador = 0
    PARAMETRO = string.lower()
    for i in PARAMETRO:
        for j in Vocales:
                if i == j:
                    contador+=1
    
    print( len(PARAMETRO) - contador)

excludes_vowel_counter("MARIA")
