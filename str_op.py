s = "У лукоморья 123 дуб зеленый 456"

def sss(s):
    if s.find("я"):
        return s.index("я")
    else:
        return 'Данная буква не найдена!'
print ('Позиция буквы "я" в строке: ', sss(s))

def sss(s):
    if s.find("у"):
        return s.count("у")
    else:
        return 'Данная буква найдена!'
print ('Буква "у" встречается в строке', sss(s), 'раз(а)!')

def sss(s):
    if s.isalpha():
        return 'Это действительно строка!'
    else:
        return s.upper()
print (sss(s))

def sss(s):
    if len(s) > 4:
        return s.lower()
    else:
        return s
print (sss(s))

def sss(s):
    return s.replace("У", "O")
print (sss(s))
