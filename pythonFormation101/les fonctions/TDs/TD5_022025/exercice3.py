
'''
fonction fibonacci 

U(n) = 0  --> U0=1
       1      U1 = 1
       n  Un = Un-1  + Un-2 
       n = 5 
       n 5 = f4 + f3 
             f3 + f2  f1 + f2 
       f2+f1   f1 + f0 f1 f1 f0
f0 f1  = f1 , f1+f0
     '''     
# Q a : 
def fibo(n):
    u0 , u1 = 1 , 1 
    for i in range(n):
        f0 , f1 = f1 , f0 +f1   #~O(1)*n  = O(n)
    return f0



# Q b : 

"""
     f(n) -> f(n-1 ) + f(n-2)
                /\         /\
                n-2 n-3   n-3 n-4 

                n=0   ou n=1 
                """
def fibo_recursive(n):
    if n == 0 or n == 1:  # 
         return 1
    return fibo_recursive(n-1) + fibo_recursive(n-2)

# O(2^N)
  
 