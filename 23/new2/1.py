for x in '0123456789ABDCDEF':
    d1=int('9009'+x,18)
    d2=int('2257'+x,18)
    d3=d1+d2
    if d3%15==0:
        print(d3//15)
# ответ 77888