a = int(input('Введите целое число: '))
def evenQ(a):
    if (a % 2) == 0:
        return 'четно'
    else:
        return 'нечетно'
    
print('Число ', evenQ(a))
