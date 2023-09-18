number=15+2**10+16
def letter(num):
    if num>9:
            if num == 10: return "A"
            if num == 11: return "B"
            if num == 12: return "C"
            if num == 13: return "D"
            if num == 14: return "E"
            if num == 15: return "F"
    else:
        return False
b=[]
while number:
    if letter(number%16) == False:
        b.append(number%16)
    else:
        b.append(letter(number%16))
    number//=16
print(b.count("F"))