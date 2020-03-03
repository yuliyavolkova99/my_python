import random
n = random.randint(1,9)
s = str(input('Какой сегодня день недели: '))

def str_n(s,n):
    if len(s) > n:
        return s.upper()
    else:
        return s
print (str_n(s,n))
