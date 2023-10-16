def t(a,b):
    for i in range(1,10000000000):
        if a%i==0 and b%i==0:
            s=i
            return s
a,b=map(int,input().split())
print(t(a,b))