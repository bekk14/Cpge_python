"""
exercice 4 : 
Algorithme de l’exponentiation rapide, qui utilise 
le concept de diviser pour régner afin de calculer x^n.
Cet algorithme repose sur les formules suivantes :
# x^n = match  n with 
#       |  0 -> 1
#       |  1 -> x
#       |  n -> a^2 si n est pair, avec a = x^(n/2)
#              x * a^2 si n est impair, avec a = x^((n−1)/2)



# a) Écrire une fonction récursive puissanceRec(x, n)
#  qui retourne la valeur x^n .
# b) Donner la complexité de cette fonction dans le pire des cas
"""

def puissanceRec(x, n):
    if n == 0:          # cas de base 
        return 1      # x^0 = 1 sortir de la récursion dierctement
   
    if n % 2 == 0:  # si n est pair
        a = puissanceRec(x, n//2)
        return a * a
    else: # Si n est impair
        a = puissanceRec(x, (n-1)//2)
        return x * a * a
# la complexité de cette fonction est O(log(n)) dans le pire des cas
# car on divise n par 2 à chaque appel récursif



"""
Remarque :
    Pour comprendre comment la pile d'appels récursifs se déploie, 
    prenons un exemple avec x = 2 et n = 5.

    puissanceRec(2, 5)
    -> Puisque 5 est impair, on calcule 2 * puissanceRec(2, 2)^2
        -> puissanceRec(2, 2) -> 2eme appel récursif
            -> Puisque 2 est pair, on calcule puissanceRec(2, 1)^2
                -> puissanceRec(2, 1) -> 3eme appel récursif
                    -> Puisque 1 est impair, on calcule 2 * puissanceRec(2, 0)^2
                        -> puissanceRec(2, 0) -> 4eme appel récursif
                            -> Puisque 0 est le cas de base, on retourne 1
                    -> On retourne 2 * 1^2 = 2   <- 
            -> On retourne 2^2 = 4
        -> On retourne 2 * 4^2 = 32

    Ainsi, puissanceRec(2, 5) retourne 32.
"""