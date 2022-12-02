# Вычислить число c заданной точностью d
import math

d = input('Введите точность числа: ')
accuracy = len(d) - 2

print(round(math.pi, accuracy))