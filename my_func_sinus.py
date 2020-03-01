import math
x = float(input('Введите вещественное число (например, 2.5): '))
def my_func_sinus(x):
    if 0.2 < x < 0.9:
        return math.sin(x)
    else:
        return 1
print (my_func_sinus(x))
