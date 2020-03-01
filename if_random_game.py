import random
a = random.randint(1,4)
b = int(input('Введите число от 1 до 4: '))
def gsch(a,b):
    if a == b:
        return ('Победа!')
    elif a > b:
        return ('Повторите еще раз! Выбранное вами число меньше загаданного случайного!')
    else:
        return ('Повторите еще раз! Выбранное вами число больше загаданного случайного!')
print(gsch(a,b))




