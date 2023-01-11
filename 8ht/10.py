def gcheck(letter): # Функция проверки гласных
    gals=("а","о","у","э","ы","я","ё","е","ю","и")# Список гласных
    if letter.lower() in gals: # Условия проверки буквы в списке. Все слова преобразуються в нижний регистр за счёт lower()
         return True
    else:
        return False
for word in "Мария","Гурий","Арсен","Борис","Игнат":
    WordL=list(word)# Разбитие слова на буквы и добавление их в список WordL
    let1=WordL.pop(1)# Вторая буква
    len1 = len(WordL) - 1  # Индекс последней буквы
    print(let1)
    if not(gcheck(WordL.pop(len1))==False) or not(gcheck(let1)==True):
        pass
    else:
        print(word)
# Гурий Борис 