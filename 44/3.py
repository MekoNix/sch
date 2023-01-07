num=int(input())
result=0
for i in range(len(str(num))//4):
    somenumber=num%10000
    newnumber= (somenumber//1000)*1000 + ((somenumber//100)%10)*10+ ((somenumber//10)%10)*100+somenumber%10
    resulat = newnumber / 10000
    result=resulat*10000+result/10000
    num=num//10000
print(result)
while result%10 !=0: result = result*100
print(int(result//100))