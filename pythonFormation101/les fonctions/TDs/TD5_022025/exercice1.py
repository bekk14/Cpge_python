"""
Écrire une fonction itérative factorielle(k)
 qui retourne la valeur de k!.
"""
#== Q a =

def factorielle(k):
     # sa complexite est la somme totale
     #  de ces instructions 
     #  O(1)+O(k)+k*O(1) = O(k)+O(k)
     #                   = O(2k) = O(k) 
     # pour k aller vers l'infini +inf 
    '''
     k!= k*(k-1)*(k-2)*...*1
     exemple : 5! = 5*4*3*2*1 = 120
    '''
    res = 1   # O(1)
    for i in range(1,k+1): #  O((k+1)-1)
        res = res * i  #O(1) 
    return res   #O(1)


#== Q b =

"""
Déterminer le nombre de multiplications qu’effectue factorielle(k). Donner la complexité
de cette fonction.
On considère la fonction suivante nommée mystere :
"""
def mystere(n):
    s = 0
    for k in range(1, n+1):
        s = s + factorielle(k)
    return s

#== Q c ==
def mystere(n):
    s = 0   # intialisation donc O(1)
    for k in range(1,n+1):  # itre n fois  donc : O(n)
        s = s +  factorielle(k) # O(1) + O(k) = O(k)
                                # car la fonction factorielle(k) 
                                # a chaque iteration de la boucle effectue 
                                # une multiplication pour chaque int de 1 a k 
                                # O(k)
    return s  # O(1)
# donc la complexite de mystere(n) 
# = O(1)+O(n)*O(k)+O(1) = O(1)+O(n)*O(k) = O(n*k)
# = O(n^2)  car k = n  pour n tend vers l'infini +inf
# et k tend vers n  donc k = n
# donc O(n^2) = O(n*n) = O(n^2)
# donc la complexite de mystere(n) est quadratique

#== Q d =
"""
Proposer une amélioration de la fonction mystere 
afin d’obtenir une complexité linéaire O(n) 
"""

def mystere(n):
    s = 0 # O(1)
    fact = 1 # O(1)
    for k in range(1,n+1):#  O(n) quand n tend vers +inf 
       fact = fact * k  # operation puis affectation donc O(1+1)~O(1)
       s = s +  fact     # operation puis affectation donc O(1+1)~O(1) 
    return s #O(1)
# donc la complexite de mystere(n)  samplifeir pour etre
# = O(1)+O(n)*(O(1)+O(1)) = O(1)+O(n)*O(1) = O(n)
# donc la complexite de mystere(n) est lineaire O(n)

""" Remarque :
Complexité unitaire : O(1)
+  Les opérations de base: (+, -, *, /, %, etc.) 
+  et les opérations d'affectation = 
=> notée O(1)

Règles
!!! Somme des complexités : 
    Lorsqu'on a plusieurs instructions séquentielles,
    on additionne leurs complexités. Par exemple, O(1)+O(k)=O(k)

Produit des complexités :
     Lorsqu'une opération est répétée dans une boucle,
     on multiplie la complexité de l'opération par
     le nombre d'itérations.
     Par exemple, une opération O(1) répétée k fois donne O(k)

Simplification :
 On ignore les constantes multiplicatives et les termes de moindre ordre.
    Par exemple, 
    ** O(2k) se simplifie en O(k)
    ** et O(n^2+n) se simplifie en O(n^2)

Majorer et minorer la complexité :

Majorer (borne supérieure) :
!!! On cherche à déterminer la complexité dans le pire des cas.
    Par exemple, la fonction factorielle(k) a une complexité majorée par O(k).

Minorer (borne inférieure) : 
On peut aussi chercher à déterminer la complexité dans le meilleur des cas,
mais en pratique, on se concentre souvent sur la majoration pour garantir 
que l'algorithme sera efficace même dans le pire scénario.

Amélioration de la complexité :

Dans l'exercice, la fonction mystere(n) a été améliorée pour passer d'une complexité
quadratique O(n^2) à une complexité linéaire O(n).
Cela a été réalisé en évitant de recalculer la factorielle à chaque itération 
et en utilisant une variable intermédiaire (fact) pour stocker la valeur
 de la factorielle courante.
"""




