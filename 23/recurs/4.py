def f(s, t):
    if s ==t:
        return 1
    if s > t:
        return 0
    if s==12:
        return 0
    return(f(s+1,t) + f(s*2, t))
print(f(3,20) * f(20,30))