n=int(input())
for i in range(1,n+1):
    lsI=list(str(i))
    try:
        for nm in lsI:
            if i%int(nm) == 0:
                ch=True
            else:
                ch=False
    except ZeroDivisionError:
        ch=False
        pass
    if ch==True: print(i)