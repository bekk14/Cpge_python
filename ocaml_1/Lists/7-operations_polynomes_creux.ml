(******************
Operations sur les polynomes creux
******************)
#
let p = [(1,0);(2,3)]   (* (a,degre) -> 1 + 2X^3 *)
# -> p : (int * int ) List 
let p2 = [(3,0); (2,2); (5,10)];

let rec do_list f  = function 
  | [] -> ()
  | x :: l -> f x ; do_list f l ;;

let imprime_monome a degre = 
  Printf.printf " %dx^%d" a degre
let imprime_polynome_creux p =
  do_list (function (a,degre) -> imprime_monome a degre) p ;;

#addition des polynomes creux 
p1 = 1x0 2x1 3x2 ... 
p2 = 1x0 2x1 4x3 ...
add p p = (1+1)x0 + (2+2)x1 + (3)x2 +(4)x3 ...
 puisque p(int*int list ) 
         si p1!= [] et p2= [] -> p2
         si p1= [] et p2!=[] -> p1
         compare les degrees de chaque element simultaniment 
          p(t1::r2) p2(t2::r2) -> t1(a,d) as m1  and t2(a,d) as m2
                       
let rec ajoute_polynome_creux p1 p2 = 
  match p1 , p2 with 
  | _ , [] -> p1
  | [] , _ -> p2
  | (a1,degre1 as m1) :: reste1, (a2,degre2 as m2):: reste2 ->
    if degre1 = degre2 
      then ((a1+a2),degre1) :: ajoute_polynome_creux reste1 reste2 
  else if degre1 < degre2 
    then m1 :: ajoute_polynome_creux reste1 p2
    else m2 :: ajoute_polynome_creux p1 reste2 ;;


utop # imprime_polynome_creux (ajoute_polynome_creux p p2) ;;
4x^0 2x^2 2x^3 5x^10- : unit = ()

(*
Multiplication des polynomes creux

*)
 
soit p : a0*x^0+a1*x^1......an*x^n   => m1+reste1 
         | m0;m1:: m2 :: m3 :: ...:: m_n::[]  or m1=(a,degre)

     p2 : a0*x^0+a1*x^1......an*x^n  => m2+reste2  or m2=(a,degre)
P1*P2 = m1*P2 + reste1*P2 

let rec map f = function 
    | [] -> []
    | x::l -> f x :: map f l ;; 

let mult_p_par_monome (a1,degre1) p = 
     map ( function (a,degre) -> (a*a1,degre1 + degre) ) p ;; 


     utop # p2;;
     - : (int * int) list = [(3, 0); (2, 2); (5, 10)]
     utop # mult_p_par_monome (2,1) p2;;
     - : (int * int) list = [(6, 1); (4, 3); (10, 11)]

let rec mult_polynome_creux p1 p2 =
  match p1 , p2 with 
  | (_ , []) -> []
  | ([], _ ) -> []
  | (m1 :: reste1), _ -> 
    ajoute_polynome_creux (mult_p_par_monome m1 p2) (mult_polynome_creux reste1 p2);;

    let p1 = (1,0)::(1,50)::[]
    
    imprime_polynome_creux (mult_polynome_creux p1 p2) ;;
    3x^0 2x^2 5x^10 3x^50 2x^52 5x^60-