num = int(input())
if num//100 == int(str(num%100)[::-1]):
    print("Да")
else:
    print("Нет")