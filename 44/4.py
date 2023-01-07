num=  int(input())
newnum= num%10000
somenumber= newnum%100
newnumber= somenumber+(newnum//100)/100
num=num//1000
print(int(newnumber*100))