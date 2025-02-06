
from collections import namedtuple
import collections
import tkinter as tk 


def f(x):


    return par, par2 , par3 

xxx= f(1)
xxx=(par,par2,par3)

tour_eiffel = 48.85826, 2.2945, 'Tour Eiffel', 'Paris'
print(tour_eiffel[0])
ntuple = (1.5 , "mots",(1,"c"),"fin")

tourEiffel = {
          "latitude": tour_eiffel[0],
          "longitude" : tour_eiffel[1],
          "nom" : "Tour Eiffel",
          "ville" : tour_eiffel[3]
        
}

tourEiffel["latitude"]

monument = namedtuple("t","latitude longitude nom ville") 



tourEiffel = monument(48.85826, 2.2945, 'Tour Eiffel', 'Paris')
tourHassan= monument(105.2,60.20,"Tour Hassan","Rabat")



tourEiffel.longitude
tourHassan.longitude









from typing import NamedTuple

class Monument(NamedTuple):
    latitude: float
    longitude: float
    nom: str
    ville: str

tr = Monument(48.85826, 2.2945, 'Tour Eiffel', 'Paris')







# array
import sys

liste = [3.14 for i in range(1_000)]
print(sys.getsizeof(liste)/1024.)
#print(liste)

import numpy as np 




print(np.cos(1))


liste = [3.14 for i in range(100)]

Tab = np.array(liste,dtype=int)

Tab.astype(float)

[ 0  0 0 ]

grid = np.zeros((2,4))

grid_list = [[1. for _ in range(4)] for i in range(2)]


grid2 =np.empty((9,9))
grid3 = np.ones((9,9),dtype=int)

range(0,9)

t=np.array(np.arange(0,10,2))

x=np.linspace(10,20,5)
 [a,b,h] => h=b-a/n    linspace(a,b,n) a+h ,a+2h, ...b 

np.shape(grid2)
np.ndim(grid3)
np.size(grid3) # n*m

# access tab[ iligne , iclonne] = cell(i,j)
grid3[ : , : ]
grid3[ i_line:j_line , i_c: j_c ]

#
grid3[1,:] = [1,2,3,4,5,6,7,8,9]
grid3[:,1]=np.array(np.arange(10,19)) #np.arange(10,19) = range(10,19)

grid3[4:6,4:6]=[[20,21],[30,31]]


grid3[4:6,4:6]=np.arange(10,19)
"""
  File "<string>", line 1, in <module>
ValueError: could not broadcast input array from shape (9,) into shape (2,2)

"""

##########
np.sum(grid3[4:6,4:6])
np.prod(grid3[-1])
np.min()
np.max()
np.var()


import numpy.linalg as la 




import matplotlib.pyplot as plt
 
x= np.linspace(0,100,10)
y = np.arange(10)
plt.plot(x,y)
plt.show()



def plot_graph():
    # Read the filename from the file_path_text widget
    filename = file_path_text.get("1.0", tk.END).strip()
    




    # Read the data from the file
    data = []
            "./data.txt", 'r','w','w+','a'
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('#'):
                columns = line.split() 
                if len(columns) >= 6:
                    data.append([float(col) for col in columns[:6]])

"""
# temperature Energy Potential Kentik temps  h 
 


"""



    # Convert the data to a numpy array
    data = np.array(data).T  # Transpose the array to separate columns
    # Extract relevant columns
    iteration, time, energy_total, kinetic_energy, energy_potential, mean_temp = data

    # Set figure size
    width = 10
    height = 6

    # Create the plot
    fig, ax = plt.subplots(figsize=(width, height))

    # Customize spines and add grid
    for spine in ax.spines.values():
        spine.set_edgecolor('#666666')
        spine.set_linewidth(1.25)
    ax.grid(color='#666666', linestyle=':', linewidth=0.5)

    # Plot the energy column as a function of the time column
    ax.plot(time, energy_potential, label='Potential Energy', color='b')  # Use a specific color

    ax.set_xlabel('Time [ps]', fontsize=12, weight='bold')
    ax.set_ylabel('Energy [Ry]', fontsize=12, weight='bold')
    ax.axvline(x=0.0, linewidth=0.5, color='k', linestyle=(0, (8, 10)))
    ax.set_xlim(0,)
    ax.set_title('Potential Energy vs. Time', fontsize=14, weight='bold')
    ax.legend()
    ax.grid(True)

    # Convert the plot to a Tkinter canvas-compatible object
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()
#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, filedialog
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



def plot_graph():
    # Read the filename from the file_path_text widget
    filename = "./filetoplt.dat"
    data = []
    with open(filename, 'r') as file:
        for line in file:                             
            if not line.startswith('#'):    
                columns = line.split()   
                if len(columns) >= 6:
                    data.append([float(col) for col in columns[:6]])
  


    # Convert the data to a numpy array
    data = np.array(data).T  # Transpose the array to separate columns
    # Extract relevant columns
    iteration, time, energy_total, kinetic_energy, energy_potential, mean_temp = data

    # Set figure size
    width = 10
    height = 6

    # Create the plot
    fig, ax = plt.subplots(figsize=(width, height))

    # Customize spines and add grid
    for spine in ax.spines.values():
        spine.set_edgecolor('#666666')
        spine.set_linewidth(1.25)
    ax.grid(color='#666666', linestyle=':', linewidth=0.5)

    # Plot the energy column as a function of the time column
    ax.plot(time, energy_potential, label='Potential Energy', color='b')  # Use a specific color
    plt.xlabel
    plt.ylabel
    ax.set_xlabel('Time [ps]', fontsize=12, weight='bold')
    ax.set_ylabel('Energy [Ry]', fontsize=12, weight='bold')
    ax.axvline(x=0.0, linewidth=0.5, color='k', linestyle=(0, (8, 10)))
    ax.set_xlim(0,)
    ax.set_title('Potential Energy vs. Time', fontsize=14, weight='bold')
    ax.legend()
    ax.grid(True)

