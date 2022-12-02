# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def primeNum (N: int):
    list_ = []
    while N > 1:
        for i in range(2,N+1):
            if (N % i) == 0:
                list_.append(i)
                N //= i
    list_.sort()
    print(list_)

number = 315
primeNum(number)