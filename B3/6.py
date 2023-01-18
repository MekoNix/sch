for x in range(0,200):
    a1 = x//100
    a2  = (x//10)%10
    a3 = x%10
    if x < 38 and not ((a1+a2+a3) !=4 ):
        print(x)
    else:
        pass