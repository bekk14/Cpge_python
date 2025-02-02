
(* fonction additionne tous les elements d'une liste
 entiers par exemple *)
 
 #  let rec somme = function 
 | [] -> 0
 | t :: r -> t + somme r ;;    
val somme : int list -> int = <fun>

exemple 

let l1 = 1::2::3::5::[];;
# let add = somme l1;;
val add : int = 11
(* represntation graphique *)
      l1             somme 1::2::3::5::[]
      ::                   |  
     /  \
     1  ::
        / \
        2  ::
          / \
          3  ::
            / \
            5  []
appel recursive de la fonction somme                   
somme [1; 2; 3; 5]
| passe
|--> 1 + somme [2; 3; 5]
1 + | passe
    |--> 2 + somme [3; 5]
        | passe
1 + 2 + |--> 3 + somme [5]
            | passe
1 + 2 + 3 + |--> 5 + somme []
1 + 2 + 3 + 5 + |--> 0 !! fin de la récursion ici
                | pas d'appel récursif
1 + (2 + (3 + (5 + 0))) = 11

(* fonction produit *)
let rec produit = function 
                | [] -> 1
                | t :: r -> x*produit r ;;
(*generalement:
la fonction s’arrete quand elle 
rencontre une liste vide

let rec f = function 
    | [] -> valeur_de_base 
    | x::l ->  f(l)

let rec f l =
         if nulle l
         then "valeur_de_base"
         else let x = tete l  and r = resete l 
             in 
               ... f(r) ... ;;
*)