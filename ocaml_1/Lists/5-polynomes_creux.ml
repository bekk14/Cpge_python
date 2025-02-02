(*
 soit le polynome  1+2X^2+3X^3 
*)
# let imprime_monome a degre =
  Printf.printf "%dx^%d " a degre
    
  ;;
val imprime_monome : int -> int -> unit = <fun>
#  let print_polynome_creux p = 
                afficher (function (a, degre) -> imprime_monome a degre) p
                ;;  
    val print_polynome_creux : (int * int) list -> unit = <fun>
# 
  let polynome = [(3, 2); (5, 1); (2, 0)];;
val polynome : (int * int) list = [(3, 2); (5, 1); (2, 0)]
# let () = print_polynome_creux polynome
  ;;
3x^2 5x^1 2x^0 