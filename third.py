# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

ourList = [1, 7, 7, 7, 6, 9, 3, 1, 2, 4, 9]
newList = []

for i in ourList:
    if ourList.count(i) == 1:
        newList.append(i)
print(newList)