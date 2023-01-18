for x in range(0,100):
    if not(x >47) and not ((x // 100) + ((x // 10) % 10) + (x % 10) >6 ):
        print(x)
    else:
        pass