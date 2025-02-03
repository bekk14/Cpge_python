(*Fonctionnelles complexes sur les listes*)

somme 
produit 
implose 
concatene_listes
@
let rec somme = function 
    | [] -> []
    | x :: l -> x somme l ;;
let rec produit = function 
    | [] -> 0 
    | x::l -> x * produit l ;;

let rec implose = function 
    | [] -> ""
    | x :: l -> x ^ implose l ;;
val implose : string list -> string = <fun>

let rec concatene_listes = function 
    | [] -> []
    | x :: l -> x @ concatene_listes l ;; 
val concatene_listes : 'a list list -> 'a list = <fun>

let rec conct_listes = function 
    | [] -> []
    | x :: l -> x :: conct_listes l ;; 
    val conct_listes : 'a list -> 'a list = <fun>

    let l=10::5::6::1::[] ; let l1=40::41::50::[]

 # conct_listes [l1;l];; 
    - : int list list = [[40; 41; 51]; [10; 5; 6; 1]]
# concatene_listes [l1;l];;
    - : int list = [40; 41; 51; 10; 5; 6;1] 