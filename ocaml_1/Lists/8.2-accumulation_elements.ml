
(***
Notion d'accumelation recursive 
***)
soit trois arguments f b et l,
comme : 
it_list f b [e1;e2;..;en] = (f(...(f(f b e1) e2) ...) en).
f a deux arguments b 1er argument  et lesements ei de list l 2eme argumenet de f 

   .... (f b e1) ....  : la valeur de b applique argument du 1er appel a f 
  ...f (f b e1) e2 ... : puis le resultats de chaque appel de f est passe en 1er arg de l'appel suivant 
  
let rec it_list f base = function 
    | [] -> base 
    | x :: l -> it_list f ( f base x ) l ;;  
    illustration graphique:

    graph l                       graph it_list f l b 
       ::            :: => f            f
      / \                              / \en 
    e1   ::                           f 
        / \                          / \en_1
       e2  ::                       f
           / \                    /  \
          en []                  b    e1

ex f est add (+) 
it_list (+) b [e1;e2;..;en] = ((+) (...((+) ( (+) b e1) e2) ...) en).
it_list + b l = b + e1 + e2 + e3 + ...  + en 
