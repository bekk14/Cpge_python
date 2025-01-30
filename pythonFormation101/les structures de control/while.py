"""
Écrire un algorithme qui lit deux entiers 
positifs A et B (B ≠ 0) et calcule le quotient
de la division entière de A par B sans utiliser
 les opérateurs : 
 Div, Mod, / et *. 
 Exemple : A = 17, B = 5 ⇒ Q = 3.
"""
A = int(input("Entrez A : "))
B = int(input("Entrez B (B ≠ 0) : "))
Q = 0
T = A
while T >= B:
    T = T - B
    Q = Q + 1
print("Le quotient est :", Q)

"""
Modifier l'algorithme de l'exercice 1 
pour déterminer aussi le reste de la division. 
Exemple : A = 17, B = 5 ⇒ Q = 3, R = 2.
"""
A = int(input("Entrez A : "))
B = int(input("Entrez B (B ≠ 0) : "))
Q = 0
T = A
while T >= B:
    T = T - B
    Q = Q + 1
R = T
print("Le quotient est :", Q)
print("Le reste est :", R)

"""
Écrire un algorithme qui décompose un entier N en 
facteurs premiers en affichant chaque facteur et sa puissance.
"""
N = int(input("Entrez N : "))
i = 2
while N > 1:
    puissance = 0
    while N % i == 0:
        N = N // i
        puissance += 1
    if puissance > 0:
        print("Facteur :", i, "Puissance :", puissance)
    i += 1

"""
Écrire un algorithme qui lit un entier N et affiche ses chiffres 
en commençant par le dernier.
 Exemple : N = 74304 ⇒ 4, 0, 3, 4, 7.
"""
N = int(input("Entrez N : "))
while N > 0:
    chiffre = N % 10
    print(chiffre)
    N = N // 10

"""
Modifier l'algorithme de l'exercice 4 pour calculer 
la somme des chiffres de N. Exemple : N = 74304 ⇒ S = 18.
"""
N = int(input("Entrez N : "))
S = 0
while N > 0:
    chiffre = N % 10
    S += chiffre
    N = N // 10
print("La somme des chiffres est :", S)

"""
Modifier l'algorithme de l'exercice 4 pour calculer
le nombre des chiffres pairs de N et celui des impairs.
Exemple : N = 73498 ⇒ NP = 2, NI = 3.
"""
N = int(input("Entrez N : "))
NP = 0
NI = 0
while N > 0:
    chiffre = N % 10
    if chiffre % 2 == 0:
        NP += 1
    else:
        NI += 1
    N = N // 10
print("Nombre de chiffres pairs :", NP)
print("Nombre de chiffres impairs :", NI)

"""
Écrire un algorithme qui lit deux entiers X et Y,
 et calcule (X^Y) en utilisant une boucle et l’opération de multiplication.\\
Rappel :
 P = X^Y = X*X*...*X (Y fois), si Y > 0 .
"""
X = int(input("Entrez X : "))
Y = int(input("Entrez Y : "))
P = 1
i = 0
while i < Y:
    P *= X
    i += 1
print("X^Y est :", P)

"""
Écrire un algorithme qui détermine les deux premiers entiers de 3 chiffres,
à partir de 100, qui sont égaux à la somme de leurs chiffres au cube.
Exemple : 153 = 1^3 + 5^3 + 3^3.
"""
N = 100
compteur = 0
while compteur < 2:
    somme = 0
    temp = N
    while temp > 0:
        chiffre = temp % 10
        somme += chiffre ** 3
        temp = temp // 10
    if somme == N:
        print(N)
        compteur += 1
    N += 1
