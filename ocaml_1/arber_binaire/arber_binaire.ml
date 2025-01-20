
(* les arbres binaires*)

structure donnes lineaires / sequentielles 
tableau access a un element a (O(1)):
  -> tableau dynamique 
  -< tableau hachage 

liste chainee : supression / ajoute en (O(1)) 
   -< liste doublement chainee
   -> list cyclique 

structure de donnes : hiearachique 
(elements  ranges  par niveau )
*   Arbre 
*   Arbre equilibre (AVL, arber rouge-noir )
        -> peremt d'ajouter  ou suprimer en O(log(n))
*   tas : permet d'implementer une file de priorite 
*   Trie (arber prefixe) : pour chercher des chaines de caracteres 
*   ...
* ARBRE BINAIRE (rec)*
une arber binaire est : 
    | soit vide {epslion}
    | soit constitue d'un noeud ( la racine) et
        deux sous-arbres binaires (gauche ; droit)

exemple  d'un arbre binaire
            (0)              : niveau 1 : le pere 
       gauche     droite
      /            \         les racines 
    (1)             (5)      : niveau 2 les peres des sous-arbers 
  /    \           /   \      
(2)     (3)      (6)    (7)  : niveau 3
       /
     (4)                     : niveau 4 
[plus profondement]      [ le profondeur ]

** parcours prefixe :appel de r; puis noeuds de g (rec ); puis noeuds de d (rec )
** parcours infixe : d'abord les noeuds de g (rec ); puis r ; puis les noeuds de d (rec)
** parcours suffixe : d'abord les noeuds de g (rec ); puis les noeuds de d (rec) ; puis r

*** arbre binaire de recherche (ABR) ***
un arbre binaire de recherche est un arbre binaire 
tel que pour chaque noeud d'etiquitte de racine r et de sous-arbres g et d ;
"
r est superieur a toutes les etiquettes des noeuds de g et inferieur a
 toutes les etiquettes des noeuds de d
 "
    - les noeuds du sous-arbre gauche de x ont des valeurs
    inferieures a celle de x
    - les noeuds du sous-arbre droit de x ont des valeurs   
    superieures a celle de x

"Un ABR est donc une structure <triee> permettant de generaliser 
la recherche par dicatomie dans un tableau trie"

*** exemple d\ABR ***
           (4)                |     R = 4 > G(3) ET < D(6) 
         gauche     droite    |
        /            \        |
      (3)             (6)     |     r(3) > g(1)  and r(6) > g(5) et < d(7)
    /               /   \
   (1)            (5)    (7)  | r(1) < g(0) et < d(2) and  
   / \                    \ 
(0)  (2)                  (8)  |   r(7) < d(8) et r(8) et < d(9) 
                            \
                             (9)
exemple 2 : 
*** exemple d\ABR ***
           (5)               
        /            \       
      (3)             (6)    
    /               /   \
   (1)            (4)    (7)  
   / \                    \ 
(0)  (2)                  (8) 
                            \
                             (9)
                         ********************************************
le noeud racine est 5 :
- le sous-arbre gauche de 5 :3,1,0,2
- le sous-arbre droit de 5 :6,4,7,8,9
le noeud de racine 3:                            le noeud de racine 6 :
- le sous-arbre gauche de 3 :1,0,2                     - le sous-arbre gauche de 6 : 4
- le sous-arbre droit de 3 :(aucun)                    - le sous-arbre droite de 6 : 7 , 8 , 9 
le noeud de racine 1:                            le neoud de racine 7 : 
- le sous-arbre gauche de 1 :0                         - le sous-arbre gauche de 7 : (aucun )
- le sous-arbre droit de 1 :2                          - le sous-arbre droite de 7 : 8,9
****************************************************************************************************

(* Arbre binaire de recherche equilibre , arbre rouge-noir *)

ARB : de hetuer h 
    - has :  test d'appartenance en O(h)
    - add :  ajouter d'un element en O(h)
    - del : supression d;un element en O(h)

=======
creation d'un arbre binaire en Ocaml : 

type ('a , 'b) arbre =
    | Fuille of  
    | 

type 'v hashtable 

    