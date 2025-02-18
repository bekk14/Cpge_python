"""
On considère la fonction mystere(n) ci-dessous
a : Décrire ce que fait cette fonction et proposer une autre solution.
b : Déterminer la complexité de mystere.
"""

from math import log 

def mystere(n):
    p=log((n),2)   #O(1)
    T=[]            #O(1)
    i , aux = 0,n    #O(1)
    while i<p:        #O(log(n))
         T.append(aux%2)   #O(1)
         aux=aux//2        #O(1)
         i=i+1            #O(1)
    return T            #O(1)
# La complexité 

# La boucle while s'exécute log2(n) fois, et à chaque itération, les opérations effectuées sont de complexité constante O(1).
# Donc, la complexité totale de la fonction est :
# O(1) + O(1) + O(1) + O(log(n)) * (O(1) + O(1) + O(1)) + O(1)
# = O(3) + O(log(n)) * O(3) + O(1)
# = O(3) + O(3 * log(n)) + O(1)
# = O(3) + O(log(n)) + O(1)
# = O(log(n))
# donc, la complexité  mystere(n) est O(log(n)).
# Cette complexité est logarithmique car la boucle while s'exécute log2(n) fois,
# ce qui correspond au nombre de bits nécessaires pour représenter n en binaire.


"""
# La fonction mystere(n) convertit un nombre entier n 
# en sa représentation binaire inversée sous forme de liste.
#  Voici une autre solution pour obtenir le même résultat 
"""
# solution 1
def mystere_alternative(n):
    T = []
    while n > 0:
        T.append(n % 2)
        n = n // 2
    return T

# autre solution 
def mystere_bin(n):
        return [int(bit) for bit in bin(n)[2:]] # O(log(n))
# tout d'abord [ _ for _ in seqs ] est une liste en compréhension 

# et 
# bin(n)='0b...' retourne une chaîne de caractères représentant 
# la valeur entière n en binaire.
# donc bin(n)[2:-1] retourne sans les deux premiers caractères '0b'

    # Q b : La complexité de mystere 
    # La complexité de la fonction mystere est O(log(n)). 
    # En effet, la boucle while s'exécute log2(n) fois,
    #  ce qui correspond au nombre de bits nécessaires 
    # pour représenter n en binaire.
# toujeurs sa complexité est O(log(n)) car la represntation binaire
# d'un nombre entiere est proportionnelle a log(n) de base 2



 
