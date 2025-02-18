
'''
On rappelle la définition de la suite de Fibonacci :
   
     U(n:int) =  match n with 
           | 0  ->    1
           | 1   ->    1
           | n   ->     U(n-1)  + U(n-2) 

     '''     
# Q a : Évaluer la complexité de la fonction fibo1(n) suivante  
def fibo(n):
    f0 , f1 = 1 , 1  # O(1)
    for i in range(n): # O(n)
        f0 , f1 = f1 , f0 +f1  # O(1+1) = O(1)
    return f0 # O(1)
# donc la complexité de fibo(n) 
# = O(1)+O(n)*O(1)+O(1) = O(n)+O(1) = O(n)
# donc la complexité de fibo(n) est linéaire O(n)




# Q b : Écrire une fonction récursive qui retourne la valeur de Fn.
#  Donner sa complexité. 

"""
La fonction récursive pour calculer la suite de Fibonacci peut être représentée sous forme d'arborescence :
tou
cas de base : n= 1 ou 0 retourne 1
sinon :
                      f(n) 
                    /         \
                f(n-1)        f(n-2)
                / \             / \
            f(n-2)  f(n-3)  f(n-3)  f(n-4)
            ..............................
            

Chaque appel de f(n) génère deux appels récursifs :
 f(n-1) et f(n-2), 
ce qui double le nombre d'appels à chaque niveau de l'arborescence.
La profondeur de l'arborescence est n, donc la complexité est O(2^n).
"""
def fibo_recursive(n):
    if n == 0 or n == 1:  # cas de base sert a arreter la recursion
         return 1          
    return fibo_recursive(n-1) + fibo_recursive(n-2) # deux appels recursifs

# O(2^N) car chaque appel de f(n) génère deux appels récursifs 
# complexite exponentielle qui est tres couteuse en terme de temps
# et d'espace

  
 