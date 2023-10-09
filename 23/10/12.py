n=int(input())
for i in range(1,n+1):
    number=i**2
    lenI=len(str(i))
    lastnumbers=number%int((10**lenI))
    if i == lastnumbers:
        print(i)