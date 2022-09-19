#!/usr/bin/python3.8

num = int(input())
if (num//10)//10 == num %10 == (num//10)%10:
    print("Все числа одинаковые")
else:
    print("Числа разные")
    