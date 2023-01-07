num = int(input())
resultnumber= 0
tenstar=len(str(num))
for i in range(tenstar//2):
    somenumber = num % 100
    reversenumber = ((somenumber % 10) * 10 + (somenumber // 10))
    resultnumber = (reversenumber*100+resultnumber/100)
    num = num // 100
while resultnumber%10 !=0:resultnumber=resultnumber*10
print(int(resultnumber//10))