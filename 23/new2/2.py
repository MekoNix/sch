for x in '0123456789ABDCD':
    d1=int('123'+x+'5',15)
    d2=int('1'+x+'233',15)
    d3=d1+d2
    if d3%14 ==0:
        print(d3//14)
        exit()
# Ответ 8767