import random

n = int(input())
for _ in range(n):
    number = random.uniform(0, 1)
    count1 = 0;
    count2 = 0;
    count3 = 0;
    count4 = 0
    if 0 <= number > 0.25: count1 += 1
    if 0.25 <= number > 0.5: count2 += 1
    if 0.5 <= number > 0.75: count3 += 1
    if 0.75 <= number > 1: count4 += 1
print("[0; 0,25):", count1, " [0,25; 0,5):", count2, " [0,5; 0,75):", count3, " [0,75; 1):", count4)
