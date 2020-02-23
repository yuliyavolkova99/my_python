def sale_one(a,b):
    if b == 'завтра':
        return float(a * 0.05)
    else:
        return a

def sale_two(a,b):
    if b >= 20:
        return float(a * 0.2)
    else:
        return a

film = input('Выберите фильм: ')
day = input('Выберите день (сегодня, завтра): ')
time = int(input('Выберите время: '))
nticket = int( input('Выберите количество билетов: '))
print('Фильм: ', film, 'День: ', day, 'Время: ', time, 'Количество билетов: ', nticket)

if film == '«Паразиты»':
    if time == 12:
        print(sale_one(sale_two(250*nticket, nticket), day))
    elif time == 16:
        print(sale_one(sale_two(350*nticket, nticket), day))
    elif time == 20:
        print(sale_one(sale_two(450*nticket, nticket), day))
    else:
        print('В данное время сеансов не найдено!')
elif film == '«1917»':
    if time == 10:
        print(sale_one(sale_two(250*nticket, nticket), day))
    elif time == 13:
        print(sale_one(sale_two(350*nticket, nticket), day))
    elif time == 16:
        print(sale_one(sale_two(350*nticket, nticket), day))
    else:
        print('В данное время сеансов не найдено!')
elif film == '«Соник в кино»':
    if time == 10:
        print(sale_one(sale_two(350*nticket, nticket), day))
    elif time == 14:
        print(sale_one(sale_two(450*nticket, nticket), day))
    elif time == 18:
        print(sale_one(sale_two(450*nticket, nticket), day))
    else:
        print('В данное время сеансов не найдено!')
else:
    print('Данного фильма в списке не обнаружено!')

        
