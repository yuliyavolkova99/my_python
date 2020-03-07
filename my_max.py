a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
def maxZ(a,b):
    if a > b:
        return a
    else:
        return b
print('Наибольшее число: ', maxZ(a,b))
