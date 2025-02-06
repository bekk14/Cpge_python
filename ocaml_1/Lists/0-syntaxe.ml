(*
creation des listes :
- [elment1;e2;..;en]  ou [] nil et :: cons= constructeur
- les elements sont separes par ;
- on n' accede pas dircetment a un element de la list 
- taille dynamique
-!!! on ajoute toujours les elements au debut d'une liste
    et non a la fin 
*)
(*liste vide []  -> est polymorphe*) 
# []
(* :: operateur infixe aui ajouter un element en tete 
      d'une liste*)
      # [];;
      - : 'a list = []
      # 0:: [10;12;50];;
      - : int list = [0; 10; 12; 50]
      # 1::11::5::3::5;;
      Error: This expression has type int but an expression was expected of type
               int list
      # 1::11::5::5::[];;
      - : int list = [1; 11; 5; 5]
      
(* Representation graphique des lites *)
let l=[e1;e2;e3;...;en]
          l
          ::
        /   \
        e1  ::
           /  \
           e2 ::
             /  \
             e3  ::
                  ...
                    \
                    ::
                    / \
                   en [] 

(* on n'acceder pas directement au elements des listes
voici qlqs fonctions tres utiles*)
(* teste si la liste est vide *)
- : int list = [1; 11; 5; 5]
# let  nulle = function 
  	     | [] -> true 
  	     | _ -> false ;;
val nulle : 'a list -> bool = <fun>
# nulle [];;
- : bool = true
# nulle [1;2];;
- : bool = false
(* pour retourner son tete  nommer par t ex*)
# let tete = function 
  	   | t :: r -> t  
  	   | _ -> failwith "tete"    
  ;;
val tete : 'a list -> 'a = <fun>
(* pour retourner son reste nommer par r par ex*)
# let reste = function 
  	    | _ :: r -> r 
  	    | _ -> failwith "reste";;
val reste : 'a list -> 'a list = <fun>

