

def Morse_Recu(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return Morse_Recu(n // 2)
    else:
        return 1 - Morse_Recu((n - 1) // 2)
    



def ThueMorseListe_mauvais(n):
    T = [0] * (n + 1)
    for i in range(n + 1):
        T[i] = Morse_Recu(i)
    return T




from matplotlib import pyplot as plt

import matplotlib.pyplot as plt 
