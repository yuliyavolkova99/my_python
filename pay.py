hours = int(input('Введите количество отработанных часов: '))
pay_rate = float(input('Введите значение почасовой ставки: '))
def payf(hours, pay_rate):
    return hours*pay_rate
print(payf(hours, pay_rate))
