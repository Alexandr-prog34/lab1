import math
'''Подключаем библиотеку с математическими функциями'''

'''
Функция для нахождения площади круга с заданным радиусом
'''
def area(r):
    '''
    Принимает r - радиус, возвращает площадь круга с заданным радиусом
    '''
    return math.pi * r * r

'''
Функция для нахождения длины окружности с заданным радиусом
'''
def perimeter(r):
    '''
    Принимает r - радиус, возвращает длину окружности с заданным радиусом
    '''
    return 2 * math.pi * r
