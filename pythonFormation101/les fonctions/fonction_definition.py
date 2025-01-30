"""
# Introduction aux différents types de fonctions en Python
En Python, les fonctions sont un moyen d'encapsuler du code dans des blocs réutilisables.
Les fonctions peuvent prendre des arguments,
retourner des valeurs,
et peuvent être de différents types tels que :
    # - Fonctions simples 
                         | - avec arguments ou sans arguments
                         |- retournant des valeurs ou ne retournant rien
    # - Fonctions avec arguments par défaut
    # - Fonctions lambda (anonymes)
    # - Fonctions récursives
def et : sont utilisés pour définir une fonction en Python.
"""

#Fonctions simples 
def nomfonction(par:int, par2:str , par3:float )->list:
      # exp
      return [par, par2, par3]
#
def nomfonction2(par1,par2,par3):
     # instruction 
     # ...
     #
     # sans return 
#
def nomfonction3(): 
       print("Bienvenue dans notre société")

#Fonctions avec arguments par défaut
def nomfonction4(genre="homme", color="blue"):
      print("Je suis un", genre, "ma couleur préférée est", color)

#- Fonctions lambda (anonymes)
f = lambda x : x**2 


def carre(n: int , f = lambda a : a**2 ):
     print(" carre de :",n," est ",f(n))


# - Fonctions récursives
""" 
n! = n*(n-1)*....*(n-n+1)
0!=1! = 1
fac = 1
for n in range(1,n+1):
    fac = fac * n    

"""
def fac(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n - 1)
'''
fac(4)
    4*fac(3)
         3*fac(2)
            2*fac(1)
              return 1
'''       
# fonction récursive mutuelle
def paire(n: int) -> bool:
    if n == 0:
        return True
    else:
        return impaire(n - 1)

def impaire(n: int) -> bool:
    if n == 0:
        return False
    else:
        return paire(n - 1)
     

"""
        Calcule la somme des diviseurs stricts d'un nombre donné.
        Un diviseur strict d'un nombre est un diviseur qui est inférieur à ce nombre.
        Args:
            n (int): Le nombre pour lequel calculer la somme des diviseurs stricts.
        Returns:
            int: La somme des diviseurs stricts de n.
        Example:
            >>> somdivStrict(6)
            6
            # Les diviseurs stricts de 6 sont 1, 2, et 3. Leur somme est 6.
"""
def divStrict(n:int):
     """
     divStrict(8) affiche les nombres 1, 2 et 4
     """
     for _ in range(1,n):
          if (n % _ == 0 ):
               print(_ ,"div struct de ",n)
               

def somdivStrict(n:int):
     somme = 0
     for _ in range(1,n):
          if (n % _ == 0 ):
               print(_ ,"div struct de ",n)
               somme += _
     return somme