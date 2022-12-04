# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def CoeffIndex (list_):
    listOfKoef = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in list_:
        if '^' in i:
            if i.find('x') > 0:
                listOfKoef[int(i[-1])] = int(i[:i.find('x')])
            else:
                listOfKoef[int(i[-1])] = 1
        elif i.find('x') > 0:
            listOfKoef[1] = int(i[:i.find('x')])
        elif i.find('x') == 0:
            listOfKoef[1] = 1
        else:
            listOfKoef[0] = int(i)
    return listOfKoef

def sumOfPolynoms(listOne: list, listTwo: list):
    newList = []
    listOfStr = []
    strOfSum = ''
    for i in range(10):
        newList.append(listOne[i]+listTwo[i])
    for k in range(9, -1, -1):
        if newList[k] > 1:
            if k > 1:
                listOfStr.append(str(newList[k])+'x^'+ str(k))
            elif k == 1:
                listOfStr.append(str(newList[k])+'x')
            else:
                listOfStr.append(str(newList[k]))
        elif newList[k] == 1:
            if k > 1:
                listOfStr.append('x^' + str(k))
            elif k == 1:
                listOfStr.append('x')
            else:
                listOfStr.append('1')
    return listOfStr

TextFileFirst = r'firstfile.txt'
with open(TextFileFirst, 'r') as firstFile:
    firstPoly = firstFile.read()

TextFileSecond = r'secondfile.txt'
with open(TextFileSecond, 'r') as secondFile:
    secondPoly = secondFile.read()

firstPolyList = firstPoly[:firstPoly.find(" =")].split(' + ')
secondPolyList = secondPoly[:secondPoly.find(" =")].split(' + ')
result = r'ResultFile.txt'
with open(result, 'w') as resultFile:
   resultFile.write(' + '.join(sumOfPolynoms(CoeffIndex(firstPolyList), CoeffIndex(secondPolyList))) + ' = 0')