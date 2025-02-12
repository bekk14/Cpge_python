





#== Q a =

def factorielle(k): # O(k)
    '''
     k!= k*k-1*k-2.....*1
     4! = 4*3*2*1
     1*2*3*4
     fac = 1
     1 ------ 4 
     fac = fac * i 
    '''
    res = 1   O(1)
    for i in range(1,k+1): # 1 2 3 4 5 ... k
        res = res * i    
    return res   


#== Q b =

O(n)

#== Q c ==
def mystere(n):
    s = 0   ~ O(1)
    for k in range(1,n+1):  # 1  n -> +inf  O(n)
        s = s +  factorielle(k) # 1 2 3  ---- n  
    return s 
n*O(1)*O(n) ~ O(n^2)




#== Q d =
# 4 = 1! + 2! + 3! + 4! 

def mystere(n):
    s = 0 
    fact = 1 
    for k in range(1,n+1):#  k 1 -> inf 
       fact = fact * k  #~ O(1) 
       s = s +  fact     #~ O(1)     =  C0   (n+1-1)=n 
    return s 




