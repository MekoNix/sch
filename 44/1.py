num = input()
newnumber=0
for i in range(len(num)):
    num=int(num)
    number = num%10
    num = num//10
    newnumber = newnumber*10+number
print(newnumber)
