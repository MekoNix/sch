n=int(input())
ctn=0
while n>0:
    if n%2==0:
        ctn+=1
    n/=10
print(ctn)