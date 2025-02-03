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

let  rec iterateur_sur_listes f b = function 
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
let somme l = iterateur_sur_listes (+) 0 l ;;
