#!/usr/bin/python3.8
import random
a = []
b = []
for  i in range(100,200):
    a.append(random.randint(100,200))
print(a)
for i in a:
    b.append(a{i+1}+a[i])

print(max(b),min(b))