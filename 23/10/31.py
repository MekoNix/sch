n=int(input())
for x in range(1,n+1):
    summ=0
    for i in range(1,n):
        if x%i ==0:
            summ+=i
    if summ ==n:
        print(x)