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
        return 1
   
    if n % 2 == 0:  
        a = puissanceRec(x, n//2)
        return a * a
    else:
        a = puissanceRec(x, (n-1)//2)
        return x * a * a
# la complexité de cette fonction est O(log(n)) dans le pire des cas
# car on divise n par 2 à chaque appel récursif
