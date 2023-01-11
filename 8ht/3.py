count = 0
def gcheck(letter): # Функция проверки гласных
    gals=("а","о","у","э","ы","я","ё","е","ю","и")# Список гласных
    global count# Берём count из всего когда
    if letter.lower() in gals: # Условия проверки буквы в списке. Все слова преобразуються в нижний регистр за счёт lower()
         count+=1
         return True
    else:
        count+=0
        return False
for word in "Есенин","Одоевский","Толстой","Фет","Астафьев": # Перебор всех Слов
    WordL=list(word)# Разбитие слова на буквы и добавление их в список WordL
    for i in WordL:
        gcheck(i)
    if not(count%2 ==0 ) and not(gcheck(WordL.pop(0)) ==False): # WordL.pop(0) - 	Удаляет 0-ый элемент и возвращает его.
       print(word)
    count=0 # Обнуляем счётчик тк как в функции он будет прибавляться.
# Есенин Астафьев
