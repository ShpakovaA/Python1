year = int(input("Введите год "))
def leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print('Это высокосный год')
    else:
        print('Это обычный год ')
leap_year(year)