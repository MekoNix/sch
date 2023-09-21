for x in '0123456789ABCDEFG':
    b=[]
    d1=int('3B8'+x+'1',17)
    d2=int('2'+x+'9'+x+'3',17)
    dsumm=d1+d2
    while dsumm !=0:
        b.append(dsumm%6)
        dsumm//=6
    if b.count(5) == 3:
        print(x)
        break
#Ответ C
