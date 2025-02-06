
(***
Notion d'accumelation recursive 
***)
*** d'autre schema recursif revient 
    souvent est accumelation 
    ****

let rec somme_accu accu = function 
    | [] -> accu 
    | x :: l -> somme_accu (x + accu) l ;;
    
    val somme_accu : int -> int list -> int = <fun>
    # let add_l l= somme_accu 0 l ;;   accumelateur initialement par 0 
    val add_l : int list -> int = <fun>
    # add_l l1;;
    - : int = 132
    # 

(*fonction generale*) 
let rec accumulateur_sur_listes f accu = function    (* equivalent a it_list*)
    | [] -> accu 
    | x :: l -> accumulateur_sur_listes f (f x accu)  l ;;
        val accumulateur_sur_listes : ('a -> 'b -> 'b) -> 'b -> 'a list -> 'b = <fun>
ex 
let somme_accu l = accumulateur_sur_listes (function x -> function accu -> x + accu ) l ;; 
let somme l = somme_accu 0 l;;
somme [12;22;22;1];;
- : int = 5
let poduit_accu l = accumulateur_sur_listes (function x -> function accu -> x * accu ) l ;;
let produit l = produit_accu 1 l;; 