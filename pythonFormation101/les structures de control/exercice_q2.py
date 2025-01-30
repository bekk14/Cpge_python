import random  

distance_total = 0

a , b = 0 , 5 

for _ in  range(1,101):
    pas = random.uniform(a,b)
    distance_total += pas 
    #print(f"pas {_} : distance parcourue depuis le départ = {distance_total} cm")
    print("index = ",_," pas= ",pas," distance = ",distance_total)


distance_total = 0
i =0 
while distance_total < 250 :
     pas = random.uniform(a,b)
     distance_total += pas
     i +=1
     print("index = ",i," distance = ",distance_total)