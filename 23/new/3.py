for x in '0123456789ABCDEF':
    d1=int('10'+x+'A',16)
    d2=int('FF'+x+'78',16)
    if (d1+d2)%19 ==0:
        print((d1+d2)//19)
#Ответ 55238