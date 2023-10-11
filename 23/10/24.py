numbers=[]
number=int(input())
while number !=0:
    numbers.append(number)
    number=int(input())
print("MAX:",max(numbers)," MIN:",min(numbers))