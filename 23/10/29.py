a,b= map(int,input().split())
NatNumbers=[]
PrimeNumbers=[]
for i in range(a,b+1):
    flag=0
    if isinstance(i,int):
        NatNumbers.append(i)
    for i2 in range(2,i):
        if i%i2 ==0: flag=True; break
    if flag: pass
    else: PrimeNumbers.append(i)
print("Натуральные числа: ",NatNumbers)
print("Простые числа: ",PrimeNumbers)

