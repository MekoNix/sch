def gcheck(letter): # Функция проверки гласных
    gals=("а","о","у","э","ы","я","ё","е","ю","и")# Список гласных
    if letter.lower() in gals: # Условия проверки буквы в списке. Все слова преобразуються в нижний регистр за счёт lower()
         return True
    else:
        return False
for word in "Анна","Максим","Татьяна","Егор","Антон":
    WordL=list(word)# Разбитие слова на буквы и добавление их в список WordL
    if gcheck(WordL.pop(int(len(WordL)-1))) or not(gcheck(WordL.pop(0))): # первое усолвие это последняя буква,  её номер в списке это количество букв-1.
        pass
    else:
        print(word)
# Егор Антон 