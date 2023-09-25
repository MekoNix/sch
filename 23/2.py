for x in range(32):
    ctn=0
    max=0
    d1=1*32**4+7*32**3+9*32**2+x*32+1+9*32**0
    d2=7*128**4+x*128**3+9*128**2+3*128**0
    d3=d1+d2
    while d3!=0:
        if d3%4==0:
            ctn=+1
        d3//=4
    maxcount=0
    if ctn>maxcount:
        maxcount=ctn
        max=x
print(max)
