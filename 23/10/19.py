import math
n, m = map(int, input().split())
while n >0:
    if n>m:
        n=m-n
    elif m>n:
        m=n-m
print(abs(n))