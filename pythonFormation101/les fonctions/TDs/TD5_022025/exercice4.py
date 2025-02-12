
"""
\section*{Exercice 4}
L'algorithme de l'exponentiation rapide, qui utilise le concept de diviser pour régner afin de calculer $x^n$. Cet algorithme repose sur les formules suivantes :
\[
x^n = 
\begin{cases}
1 & \text{si } n = 0 \\ 
a^2 & \text{si } n \text{ est pair, avec } a = x^{n/2} \\ 
x \cdot a^2 & \text{si } n \text{ est impair, avec } a = x^{(n-1)/2} 
\end{cases}
\]
\begin{enum}

  \item Écrire une fonction récursive \code{puissanceRec(x, n)} qui retourne la valeur $x^n$ en utilisant le principe de l'exponentiation rapide. 
  \item Donner la complexité de cette fonction dans le pire des cas. 
\end{enum}
"""

# A : 
def puissanceRec(x:int, n:int): # x^n 
    if n == 0:
        return 1
    elif n % 2 == 0:   # si n mod 2 
        a = puissanceRec(x, n // 2)   # p(x,n//2) 
        return a*a # puissanceRec(x, n // 2)  * puissanceRec(x, n // 2) 
    else:
        a = puissanceRec(x, (n - 1) // 2)
        return x * a * a
   
#   n/2 + n/2 +n ..... 1 
# O(log(n))
    
