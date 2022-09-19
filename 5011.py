#!/usr/bin/python3.8

num = int(input())
if (num//10)//10 == num %10:
    print("Число полидром")
else:
    print("число не полиндром")