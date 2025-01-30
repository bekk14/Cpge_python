'''
Les listes en Python sont des collections ordonnées et modifiables d'éléments. 
Elles peuvent contenir des éléments de types différents, 
y compris d'autres listes.
Les listes sont définies en utilisant des crochets []
 et les éléments sont séparés par des virgules.
 '''
##Méthode simple 
list1 = []  # declaration 
list2 = [1, 2, 3, 4, 5]  # declaration avec initialisation 
list3 = ['a', 'b', 'c', 'd', 'e'] 
list4 = [1, 2, 3, 'a', 'b', 'c', 1.2, True, False, [1, 2, "Hello"]]
##Méthode par compréhension  
l = [ _ for _ in range(9)]  # par compréhension de liste
# ou bien 
l = [0]*9 
## listes des listes si n*n ou n=n c'est une matrice         
matrice = [[1,2,3],[4,5,6],[7,8,9]]
## 
grid = [[_ for _ in range(9)] for _ in range(9)]
for i in range(9): # i pour les lignes
    for j in range(9): # les colonnes
        print(grid[i][j],end="  ")
    print()

'''
les listes en Python sont des objets,
et comme tous les objets en Python,
elles sont des instances de classes.
Cela signifie qu'elles possèdent leurs propres méthodes (fonctions) 
qui leur permettent de manipuler les données qu'elles contiennent.
Par exemple, les méthodes des listes 
 classe.methode(args*)
'''
list3.append('ffofo') # ajouter un element à la fin de la liste
list3.insert(2,'ffofo') # ajouter un element à un position donnée
list3.remove('ffofo') # supprimer un element
list3.pop() # supprimer le dernier element
list3.extend(['x', 'y', 'z']) # ajouter plusieurs éléments à la fin de la liste
list3.index('b') # obtenir l'index d'un élément
list3.count('a') # compter le nombre d'occurrences d'un élément
list3.sort() # trier la liste
list3.reverse() # inverser l'ordre des éléments de la liste
list3.clear() # supprimer tous les éléments de la liste


 #  convertir un iterable en list 
list_range = list(range(1,100,10))
adn="GGGATTCCAAGGA GAGGA"
list_chaine = list(adn)