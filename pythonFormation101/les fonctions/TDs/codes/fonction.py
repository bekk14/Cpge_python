
def indice(A, val):
    id=0
    while A[id] > val or val > =A[id+1]:
        id+=1
    return id
# suppose que id existe toujours sinon
# la boucle pourrait ne pas se terminer