
"""
Écrire un algorithme qui lit N entiers et calcule
le nombre de séquences croissantes parmi ces N entiers.
 Exemple : N = 9,
 les entiers saisis sont : 7, 8, 10, 2, 4, 1, 8, 14, 20.
Résultat : NS = 3 
(les séquences croissantes sont 7, 8, 10 ; 2, 4 ; 1, 8, 14, 20).
"""
N = int(input("Entrez N : "))
NS = 0
precedent = int(input("Entrez un entier : "))
croissant = False
for _ in range(N - 1):
    entier = int(input("Entrez un entier : "))
    if entier > precedent:
        if not croissant:
            NS += 1
            croissant = True
    else:
        croissant = False
    precedent = entier
print("Nombre de séquences croissantes :", NS)

"""
Écrire un algorithme qui lit 
N entiers et calcule le nombre des pairs et celui des impairs.
 Exemple : 
N=10, valeurs saisies : 0, 7, 2, 1, 4, 8, 20, 11, 14, 30
NP=6, 
NI=4.
"""
N = int(input("Entrez N : "))
NP = 0
NI = 0
for _ in range(N):
    entier = int(input("Entrez un entier : "))
    if entier % 2 == 0:
        NP += 1
    else:
        NI += 1
print("Nombre de pairs :", NP)
print("Nombre d'impairs :", NI)

"""
Écrire un algorithme qui lit 
N entiers et détermine le maximum. Exemple : 
N=6, entiers saisis : 7, 3, 4, 11, 8, 1 ⇒ Max = 11.
"""
N = int(input("Entrez N : "))
Max = -float('inf')
for _ in range(N):
    entier = int(input("Entrez un entier : "))
    if entier > Max:
        Max = entier
print("Le maximum est :", Max)

"""
Modifier l’algorithme de l’exercice 11 pour déterminer 
le maximum et son nombre d’occurrences (répétitions). Exemple : 
N=10, entiers saisis : 5, 3, 5, 2, 7, 4, 7, 7, 1, 6 
Max = 7, Nb = 3.
"""
N = int(input("Entrez N : "))
Max = -float('inf')
Nb = 0
for _ in range(N):
    entier = int(input("Entrez un entier : "))
    if entier > Max:
        Max = entier
        Nb = 1
    elif entier == Max:
        Nb += 1
print("Le maximum est :", Max)
print("Le nombre d'occurrences est :", Nb)