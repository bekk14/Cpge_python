(*

- liste vide est une liste triee;
 donc c'est le cas de base [] -> []
 - on va commencer par trier le reste de la liste a chaque fois 
   et mettre l'element `t` a la bonne place par l'appler la fonction `insere (e,l)`

 *)

let rec tri_par_insertion = function 
          | [] -> []
          | t :: reste ->  insere t (tri_par_insertion reste) ;;
val tri_par_insertion : 'a list -> 'a list = <fun>

(* la fonction insere element liste:
 cas de base : vide [] -> [element]
 cas t::r ->  si element <= t then element::x::reste
                              else x::( insere element reste) *)
let rec insere element = function 
        | [] -> [element]
        | t :: reste -> if (element <= t) then (element::t::reste)
                                          else (t::(insere element reste)) ;;
 val insere : 'a -> 'a list -> 'a list = <fun>

 (*
 ordre  <= 
 *)
 # let rec insere ordre element = function 
 | [] -> [element]
 | x :: reste as l -> if ordre element x then element :: l 
                      else x ::(insere ordre element reste);;
val insere : ('a -> 'a -> bool) -> 'a -> 'a list -> 'a list = <fun>

# let rec tri_insertion ordre = function 
             | [] -> []
             | x :: reste -> insere ordre x (tri_insertion ordre reste);;
 val tri_insertion : ('a -> 'a -> bool) -> 'a list -> 'a list = <fun>
 
 # tri_insertion (function x -> function y -> x >= y ) m ;;
 - : int list = [20; 15; 12; 4; 3; 1]
 
 # let ch="bonjour"::"comment"::"cpge"::"ocaml"::[];;
 val ch : string list = ["bonjour"; "comment"; "cpge"; "ocaml"]

 let ge_string x y = String.compare x y >= 0 ;;
 let le_string x y = String.compare x y <= 0 ;;
 tri_insertion (function x -> function y ->  ge_string x y ) ch;;
 #  tri_insertion (function x -> function y ->  get_string x y ) ch;;
 - : String.t list = ["ocaml"; "cpge"; "comment"; "bonjour"]
 tri_insertion (function x -> function y ->  le_string x y ) ch;;
 - : String.t list = ["bonjour"; "comment"; "cpge"; "ocaml"]
 