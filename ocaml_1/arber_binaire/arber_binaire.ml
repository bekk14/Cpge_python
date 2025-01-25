
(* les arbres binaires

structure donnes lineaires / sequentielles 
tableau access a un element a (O(1)):
  -> tableau dynamique 
  -< tableau hachage 

liste chainee : supression / ajoute en (O(1)) 
   -< liste doublement chainee
   -> list cyclique 

structure de donnes : hiearachique 
(elements  ranges  par niveau )
*   Arbre 
*   Arbre equilibre (AVL, arber rouge-noir )
        -> peremt d'ajouter  ou suprimer en O(log(n))
*   tas : permet d'implementer une file de priorite 
*   Trie (arber prefixe) : pour chercher des chaines de caracteres 
*   ...
* ARBRE BINAIRE (rec)*
une arber binaire est : 
    | soit vide {epslion}
    | soit constitue d'un noeud ( la racine) et
        deux sous-arbres binaires (gauche ; droit)

exemple  d'un arbre binaire
            (0)              : niveau 1 : le pere 
       gauche     droite
      /            \         les racines 
    (1)             (5)      : niveau 2 les peres des sous-arbers 
  /    \           /   \      
(2)     (3)      (6)    (7)  : niveau 3
       /
     (4)                     : niveau 4 
[plus profondement]      [ le profondeur ]

** parcours prefixe :appel de r; puis noeuds de g (rec ); puis noeuds de d (rec )
** parcours infixe : d'abord les noeuds de g (rec ); puis r ; puis les noeuds de d (rec)
** parcours suffixe : d'abord les noeuds de g (rec ); puis les noeuds de d (rec) ; puis r

*** arbre binaire de recherche (ABR) ***
un arbre binaire de recherche est un arbre binaire 
tel que pour chaque noeud d'etiquitte de racine r et de sous-arbres g et d ;
"
r est superieur a toutes les etiquettes des noeuds de g et inferieur a
 toutes les etiquettes des noeuds de d
 "
    - les noeuds du sous-arbre gauche de x ont des valeurs
    inferieures a celle de x
    - les noeuds du sous-arbre droit de x ont des valeurs   
    superieures a celle de x

"Un ABR est donc une structure <triee> permettant de generaliser 
la recherche par dicatomie dans un tableau trie"

*** exemple d\ABR ***
           (4)                |     R = 4 > G(3) ET < D(6) 
         gauche     droite    |
        /            \        |
      (3)             (6)     |     r(3) > g(1)  and r(6) > g(5) et < d(7)
    /               /   \
   (1)            (5)    (7)  | r(1) < g(0) et < d(2) and  
   / \                    \ 
(0)  (2)                  (8)  |   r(7) < d(8) et r(8) et < d(9) 
                            \
                             (9)
exemple 2 : 
*** exemple d\ABR ***
           (5)               
        /            \       
      (3)             (6)    
    /               /   \
   (1)            (4)    (7)  
   / \                    \ 
(0)  (2)                  (8) 
                            \
                             (9)
                         ********************************************
le noeud racine est 5 :
- le sous-arbre gauche de 5 :3,1,0,2
- le sous-arbre droit de 5 :6,4,7,8,9
le noeud de racine 3:                            le noeud de racine 6 :
- le sous-arbre gauche de 3 :1,0,2                     - le sous-arbre gauche de 6 : 4
- le sous-arbre droit de 3 :(aucun)                    - le sous-arbre droite de 6 : 7 , 8 , 9 
le noeud de racine 1:                            le neoud de racine 7 : 
- le sous-arbre gauche de 1 :0                         - le sous-arbre gauche de 7 : (aucun )
- le sous-arbre droit de 1 :2                          - le sous-arbre droite de 7 : 8,9
****************************************************************************************************

(* Arbre binaire de recherche equilibre , arbre rouge-noir *)

ARB : de hetuer h 
    - has :  test d'appartenance en O(h)
    - add :  ajouter d'un element en O(h)
    - del : supression d;un element en O(h)

=================================================================
=================================================================


creation d'un table de hachage en Ocaml : 
*)
 

type 'v hashtable = (string * 'v) list array ;;
let create m = if m <= 0 then invalid_arg "create"; Array.make m [] ;;
create 10 ;;
   
 (*h(s0s1...s_n-1) = sum(code(s_i) * 10^(i))   0 <= i < n*)

 let hash k = 
   let n = String.length k and  constant = 32 in 
   let rec hash h i = 
    if i = n then h else hash (constant*h + Char.code k.[i]) (i+1) in 
    hash 0 0 ;;
  
hash "hello";;
(*# - : int = 99162322*)

let bucket (h: 'v hashtable ) (k: string ) : int =
   let i = (hash k) land max_int in (* on garantit i > = 0*)
   i mod (Array.length h) 

let put (h: 'v hashtable) (k: string) (v: 'v)  : unit = 
    let rec update b = match b with 
        | [] -> [k,v]
        | (k' , _) :: b when k = k' -> (k,v) :: b 
        | e :: b -> e :: update b in let i = bucket h k in h.(i) <- update h.(i) ;;

let contains (h : 'v hashtable) (k : string) : bool = 
    let rec trouver b = match b with 
        | [] -> false 
        | (k',_) :: b when k = k' -> true 
        | _ :: b -> trouver b in 
    let i = bucket h k in trouver h.(i) ;;

let get (h: 'v hashtable) (k: string) : 'v  = 
    let rec trouver b = match b with 
        | [] -> raise Not_found
        | (k',v) :: b ->  if k = k'
               then v 
              else trouver b in trouver h.(bucket h k )
            ;;

hash "m";; 
hash "fig."
hash "l'"
hash "je"
hash "ressens"
hash "pythons"
hash "retiens"
(*
=================================================================
=================================================================
*)

(* les arbres binaires
n(E) = 0  : ensemble vide
n(N(l,x,r)) = l + n(l) + n(r) : ensemble a plusieur elements

hauteur 
h(E) = -1
h(N(l,x,r)) = 1 + max(h(l),h(r))
propriete :
t : arbre binaire ; n : nombre de noeuds ; h : hauteur
h1 +1 <= n <= 2^(h+1) -1
le nombre de sous-arbres vides de t est n+1;
*)

type 'a bintree =
    | E          (* Fuille vide *)
    | N of 'a bintree * 'a * 'a bintree (* sous-arbre de gauche*racine*droit *)

let rec longueur (t: 'a bintree) : int =
  match t with 
     | E -> 0   (* vide *)
     | N(l,_,r) -> 1 + longueur l + longueur r




     (*perfect: construit un arbre binaire parfait
         où chaque nœud est étiqueté par la hauteur*)
let rec perfect (h : int) : int bintree =
  if h = -1 then E
  else N(perfect (h-1), h, perfect (h-1))

let t = N(N(N(E,"C",E),"b",E),"A",N(E,"V",E)) ;;

let rec preorder (t: 'a bintree) = match t with 
  | E -> ()
  | N(l,x,r) ->  print_string x ; preorder l ; preorder r;



let rotate_right = function
    | N (N (t1, ku, vu, t2), kv, vv, t3) -> N (t1, ku, vu, N (t2, kv, vv, t3))
   | t -> t
  
let rotate_left = function
    | N (t1, ku, vu, N (t2, kv, vv, t3)) -> N (N (t1, ku, vu, t2), kv, vv, t3)
    | t -> t

type color = Rouge | Black 

type ('k , 'v) rbt = 
    | E 
    | N of color * ( 'k , 'v) rbt * 'k * 'v * ( 'k , 'v) rbt

let empty : ('k , 'v) rbt = E

let lbalance = function
  | (B, N (R, N (R, t1, k1, v1, t2), k2, v2, t3), k3, v3, t4)
  | (B, N (R, t1, k1, v1, N (R, t2, k2, v2, t3)), k3, v3, t4) ->
            N (R, N (B, t1, k1, v1, t2), k2, v2, N (B, t3, k3, v3, t4))
  | (c, l, k, v, r) -> N (c, l, k, v, r)
let rbalance = function
  | (B, t1, k1, v1, N (R, N (R, t2, k2, v2, t3), k3, v3, t4))
  | (B, t1, k1, v1, N (R, t2, k2, v2, N (R, t3, k3, v3, t4))) ->
        N (R, N (B, t1, k1, v1, t2), k2, v2, N (B, t3, k3, v3, t4))
  | (c, l, k, v, r) -> N (c, l, k, v, r)
let rec add (k: 'k) (v: 'v) (t: ('k, 'v) rbt) : ('k, 'v) rbt =
    match t with
        | E -> N (R, E, k, v, E)
        | N (c, l, k', v', r) ->
              if k < k' then lbalance (c, add k v l, k', v', r)
              else if k > k' then rbalance (c, l, k', v', add k v r)
              else N (c, l, k, v, r) (* on écrase la valeur *)
let add (k: 'k) (v: 'v) (t:('k, 'v) rbt) :('k, 'v) rbt =
      match add k v t with
          | E -> assert false
          | N (_, l, k', v', r) -> N (B, l, k', v', r)