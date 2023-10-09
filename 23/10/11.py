b3 = []
b4 = []

for n in range(111, 999 + 1):
    summ = 0
    listn = list(str(n))
    for i in listn:
        summ += int(i) ** 3
        print(listn, summ)
    if summ == n:
        b3.append(n)
for n in range(1111, 9999 + 1):
    summ = 0
    listn = list(str(n))
    for i in listn:
        summ = +int(i) ** 4
    if summ == n:
        b4.append(n)
print(b3, b4)
