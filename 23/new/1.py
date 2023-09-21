for x in '0123456789ABCDEFGH':
    d1=int('90009'+x,18)
    d2=int('2257'+x,18)
    if (d1+d2)%15 == 0:
        print(x,(d1+d2)//15)
#Ответ C 1148644