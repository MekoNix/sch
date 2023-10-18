def f(s, t):
    if s ==t:
        return 1
    if s > t:
        return 0
    return(f(s+1,t) + f(s*2, t)+f(s*3,t))
print(f(2,7) * f(7,28))