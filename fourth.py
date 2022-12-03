# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint

while (number := int(input('Введите число: '))) not in range(1,10):  # Ограничение по величине. Не обязательно
    print('Число должно быть больше 0 и меньше 10! Повторите ввод!')

def koef (N:int):
    list_ = []
    for _ in range(N+1):
        list_.append(randint(0,100))
    return list_

def polynomialWithKoef (list_ : list):
    listOfPoly = []
    degreeCount = len(list_)-1
    degrees = {
        1: '', 2: '\u00b2', 3: '\u00b3',
        4: '\u2074', 5: '\u2075', 6: '\u2076',
        7: '\u2077', 8: '\u2078', 9: '\u2079'
    }
    for i in list_:
        if i > 0:
            if degreeCount > 0:
                if i != 1:
                    listOfPoly.append(str(i) + f'x{degrees[degreeCount]}')
                else:
                    listOfPoly.append(f'x{degrees[degreeCount]}')
            else:
                listOfPoly.append(str(i))
        degreeCount -= 1  
    print(listOfPoly)
    return listOfPoly

polystr = ' + '.join(polynomialWithKoef(koef(number))) + ' = 0' 
fileText = r'file.txt'
with open(fileText, 'w', encoding='utf-8') as ourFile:
    ourFile.write(polystr)