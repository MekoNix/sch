#!/usr/bin/python3.8
import random
a=[]
count=0
for i in range(-2,2):
    a.append(random.randint(-100,100))
print(a)
for i in a:
    if i<0:
        count+=1
    else:
        pass 
print(count)