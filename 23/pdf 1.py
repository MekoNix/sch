number=((44+4**50)*4**25+44)*4**12+44
b=[]

while number:
    b.append(number%4)
    number//=4
print(0,"-",b.count(0))
print(1,"-",b.count(1))
print(2,"-",b.count(2))
print(3,"-",b.count(3))