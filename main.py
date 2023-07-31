import numpy as np


import random as rd


my_list= [1,2,5,3,9,6,3,0,2,7,10,4]

counter = 0
while  counter <=len(my_list):
    a=[]
    b=[]
    c=[]
    
    for i in range(1,4):
        a.append(rd.choice(my_list))
        b.append(rd.choice(my_list))
        c.append(rd.choice(my_list))


    my_array= np.array([a,b,c])
    
    counter +=1

print(my_array)