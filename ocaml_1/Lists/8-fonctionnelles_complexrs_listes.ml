(*Fonctionnelles complexes sur les listes*)

somme 
produit 
implose 
concatene_listes
@
operations infexes 

let rec somme = function 
    | [] -> 0 (*element de base  0  et op + *) 
    | x :: l -> x + somme l ;;
let rec produit = function 
    | [] -> 1  (* element de base  1  et op * *)
    | x::l -> x * produit l ;;

let rec implose = function 
    | [] -> ""   (* element de base  "" mot vide et op ^ conct String *)
    | x :: l -> x ^ implose l ;;
val implose : string list -> string = <fun>

let rec concatene_listes = function 
    | [] -> []  ( * element de base [] et @ op conct list  *)
    | x :: l -> x @ concatene_listes l ;;  (* @ concat*)
val concatene_listes : 'a list list -> 'a list = <fun>

let rec conct_listes = function 
    | [] -> []
    | x :: l ->  x :: conct_listes l ;;  (* :: cons *)
    val conct_listes : 'a list -> 'a list = <fun>


    let l=10::5::6::1::[] ; let l1=40::41::50::[]

 # conct_listes [l1;l];; 
    - : int list list = [[40; 41; 51]; [10; 5; 6; 1]]
# concatene_listes [l1;l];;
    - : int list = [40; 41; 51; 10; 5; 6;1] 
 
  

(*arg1 arg2 list_anonyme sur lequelle 
pattren matching est effectue                *)

let  rec iterateur_sur_listes f b = function    (* equivalent list_it*)
    | [] -> b (* b valeur de base // f fonction de deux args*)
    | x :: l -> f x (interateur_sur_listes f b l);;
           (* liste est traite element par element *)
(*                    
    val interateur_sur_listes : ('a -> 'b -> 'b) -> 'b -> 'a list -> 'b = <fun>
                        interateur_sur_liste(arg1:'a,arg2:'b,arg3:'b)
                                   une valeur de base de 'b 
                                   une liste de type 'a 
                                   retourner une valeur de type 'b 
*)
let somme2 l = iterateur_sur_listes (+) 0 l ;;


let rec list_length = function 
    | [] -> 0 
    | x :: l -> 1 + list_length l ;;

let list_length2 l = iterateur_sur_listes (function x -> function y -> 1 + y ) 0 l ;;

(* aussi avec concatenation :
la concatenation des listes, a l’aide d’une fonction auxiliaire devant
qui recopie une liste devant une autre.
*)
let rec devant second_list  = function 
      | [] -> second_list (* cas de base*) 
      | x :: l -> x :: devant second_list  l  ;;

let copy_devant l = iterateur_sur_listes ( function x -> function y -> x:: y) l;;
devant [4;5;6;7] [1;2;3];;
- : int list = [1; 2; 3; 4; 5; 6; 7]
# copy_devant [4;5;6;7] [1;2;3];;
- : int list = [1; 2; 3; 4; 5; 6; 7]


