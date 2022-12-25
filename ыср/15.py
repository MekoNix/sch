num = int(input())
num1 = num//100
num2 = num%10
num3 =  (num//10)%10
if num1 != num2 or num1 !=num3 or num2 !=num3:
    print("Да")
else:
    print("Нет")