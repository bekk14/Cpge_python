
(*
Faire une action sur les ´el´ements d’une liste
1- affichage des elements de la liste 
    `afficher print_int liste`
2- 
*)
let rec afficher f =  function 
       | [] -> ()
       | x :: l -> f(x) ; afficher f l ;;

       val afficher : ('a -> 'b) -> 'a list -> unit = <fun>

let l_int = 5::2::10::156::[];;
afficher print_int l_int ;;
5210156- : unit = ()

applique a tous les elements de la listes 

let rec map f = function 
      | [] -> []
      | x :: l -> f x :: map f l ;;

      val map : 'a -> 'b list -> 'c list = <fun>

#map succ l_int ;;
- : int list = [6; 3; 11; 157]
# map String.length ch;;
- : int list = [7; 7; 4; 5]
    