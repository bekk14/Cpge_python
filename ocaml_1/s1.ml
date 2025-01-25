
let hello () =
  print_endline "Hello, World!"

let square x =
  x * x

let add x y =
  x + y

let rec factorial n =
  if n = 0 then 1 else n * factorial (n - 1)

let double = fun x -> x * 2

let add_explicit (x: int) (y: int) : int =
  x + y

let apply_twice f x =
  f (f x)

let main () =
  hello ();
  print_endline (string_of_int (square 4));
  print_endline (string_of_int (add 3 5));
  print_endline (string_of_int (factorial 5));
  print_endline (string_of_int (double 10));
  print_endline (string_of_int (add_explicit 7 8));
  print_endline (string_of_int (apply_twice double 5))

let () = main ()
