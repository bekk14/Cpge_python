(*
Filtrage explicit 
*)

(* construction : match ... with *)
(*
* appel explicit au filtrage ::= match expression with filtrage 
la fonction nulle par un appel explicite au filtrage 
*)
let nulle l = 
  match l with 
  | [] -> true 
  | _ -> false ;;

#cas 1 : 
let nulle_ = function 
    | [] -> true  
    | _ -> false ;;
# conctantination de deux liste par excplicit au filtrage 
let rec concatene list1 list2 = 
     match list1 with 
    | [] -> list2
    | t::r -> t::concatene r list2 ;;
let rec conc liste2= function 
      | [] -> liste2
      | t :: r -> t :: conc r liste2 ;;

(* Filtrage simultane de deux valeurs*)

let rec  meme_longueur list1 list2 =
  match (list1,list2) with 
  | ([],[]) -> true 
  | (_ :: r1 , _ :: r2) -> meme_longueur r1 r2 
  | (_, _ ) -> false ;;

comme on peut ecrire  
match list1, list2 with 
| [] , [] -> true 
| _::r1 , _::r2 -> meme_longueur r1 r2 
| _ , _  -> flase 

