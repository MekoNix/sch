def f(s, t):
    if s ==t:
        return 1
    if s > t:
        return 0
    return(f(s+1,t) + f(s+3, t))
print(f(7,20))