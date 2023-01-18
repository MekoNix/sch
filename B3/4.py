for x in range(0,100):
    if (x<55) and not((x//100)+((x//10)%10)+(x%10) != 10):
        print(x)
    else:
        pass