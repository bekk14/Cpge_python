#!/usr/bin/env python3
"""
Écrire un programme Python qui convertit des valeurs d'énergie entre 
différentes unités (Ry, eV, Ha, bohr) en utilisant des facteurs de conversion prédéfinis.
1 Ry = 13.605693 eV = 0.5 Ha = 0.529177 bohr
1 eV = 0.0734986 Ry = 0.0367493 Ha = 0.019716 bohr
1 Ha = 2 Ry = 27.211386 eV = 0.529177 bohr
1 bohr = 1.88973 Ry = 51.422067 eV = 1.88973 Ha
le code doit excute de cette facon : 
    convert  value_numerique unite1 unite2
    convert.py 13.06    eV     Ha 
"""
import re
import sys

def convert_energy(valeur, from_unit, to_unit):
    conversion_factors = {
        'Ry': {
            'eV': 13.605693,
            'Ha': 0.5,
            'bohr': 0.529177
        },
        'eV': {
            'Ry': 0.0734986,
            'Ha': 0.0367493,
            'bohr': 0.019716
        },
        'Ha': {
            'Ry': 2,
            'eV': 27.211386,
            'bohr': 0.529177
        },
        'bohr': {
            'Ry': 1.88973,
            'eV': 51.422067,
            'Ha': 1.88973
        }
    }

    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        conversion_factor = conversion_factors[from_unit][to_unit]
        return float(valeur) * float(conversion_factor), conversion_factor  
    else:
        return None 
    
energy = 0.
if len(sys.argv) >= 3:
    energy = float(sys.argv[1])     
    unit1 = sys.argv[2]
    unit2 = sys.argv[3]
else:
    # print(" Please provide three args as energy unit1 unit2 | eV Ha Ry ")
    energy = float(input("Donnez la valeur de l'énergie à convertir : "))
    unit1 = input("Sélectionnez l'unité de départ (Ry, eV, Ha, bohr) : ")
    unit2 = input("Sélectionnez l'unité de destination (Ry, eV, Ha, bohr) : ")

converted_result = convert_energy(energy, unit1, unit2)

if converted_result:
    print("Résultat converti :", str(energy), str(unit1), "-->", converted_result[0], str(unit2), "par facteur", converted_result[1])
else:
    print("Erreur : Conversion non valide.")