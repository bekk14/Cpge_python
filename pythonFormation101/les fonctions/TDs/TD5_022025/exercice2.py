
# Q a 

from math import log 

def mystere(n):
    p=log((n),2)
    T=[]
    i , aux = 0,n
    while i<p:
         T.append(aux%2)
         aux=aux//2
         i=i+1
    return T


# autre solution 
def mystere(n):
  
    return T


# Q b : La complexité de mystere 

