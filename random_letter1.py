import random
a = ['самовар', 'весна', 'лето']
b = random.choice(a)
c = random.choice(b)
d = list(b)
e = b.index(c)
d[e] = "?"
f = "".join(d)
print(f)
d = str(input('Введите пропущенную букву: '))
  
def random_letter1(b,c,d):
    if d == c:
        return 'Победа!'
    else:
        return 'Увы! Попробуйте в другой раз'
print (random_letter1(b,c,d))
print ('Загаданное слово:', b)

