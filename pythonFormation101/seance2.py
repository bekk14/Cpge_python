# Table de correspondances des caractères ASCII
# (extrait)

def horner(elt: str) -> int:
          "Calcule la valeur d'un entier en suivant le schéma de Horner."
          result = 0
          for digit in elt:
                    result = result * 10 + (ord(digit) - ord("0"))
          return result

def ascii_table() -> None:
            "Affiche la table de correspondances des caractères ASCII."
            for i in range(32, 127):
                        print(f"{i:3} {chr(i)}", end=" ")
                        if i % 8 == 7:
                                    print() 
            print() 

def main() -> None:
            "Fonction principale."
            ascii_table()
            print(horner("12345"))
            print(horner("67890"))
            
if __name__ == "__main__":
            main()
 