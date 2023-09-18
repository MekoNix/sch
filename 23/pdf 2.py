number=5**44+5**555-5
b=[]

while number:
    b.append(number%5)
    number//=5
print(0,"-",b.count(0))
print(1,"-",b.count(1))
print(2,"-",b.count(2))
print(3,"-",b.count(3))
print(4,"-",b.count(4))