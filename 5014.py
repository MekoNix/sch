#!/usr/bin/python3.8
a = int(input())
b = int(input())
x = int(input())
if a>b:
    
    if x<= a and x>=b:
        print("Число ",x,"принадлежит отрезку ",b,a)
    else:
        print("Число ",x," не принадлежит отрезку ",b,a)
elif  a<b:
    if  x>= a and x<=b:
        print("Число ",x,"принадлежит отрезку ",a,b)
    else:
         print("Число ",x," не принадлежит отрезку ",a,b)
    