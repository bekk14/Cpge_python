#!/usr/bin/env python3
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
        return float(valeur) * float(conversion_factor) ,conversion_factor  
    else:
        return None 
    return None 


#print(sys.argv)
energy = 0.0
if len(sys.argv) >=3 :
     energy = float(sys.argv[1])     
     unit1 = sys.argv[2]
     unit2 = sys.argv[3]
else :
    print("Error: Please provide three args as energy unit1 unit2 | eV Ha Ry ")
    energy=float(input("give the valuer of energy to converted   : "))
    unit1=input("select which unit: Ry eV Ha : ")
    unit2=input("select unit want : Ry eV Ha : ")


converted_result = convert_energy(energy, unit1, unit2)



print("Converted result:", str(energy),' ',str(unit1),' --> ', converted_result[0], str(unit2), ' by factor ',converted_result[1])