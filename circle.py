import math

def area(r):
    ''' Высчитывается площадь круга с радиусом равным r
            Агрумент r (int) равен радиусу окружности
            Возвращаемое значение area(r):(float) Площадь круга с радиусом (r)
    Пример запуска:
        area(3)
        >> 28,274333882308139146163790449516
    '''
    return math.pi * r * r


def perimeter(r):
    ''' Высчитывается длина окружности с радиусом равным r
            Агрумент r (int) равен радиусу окружности
            Возвращаемое значение perimeter(r): длина круга с радиусом (r)
    Пример запуска:
        perimetr(3)
        >> 18,849555921538759430775860299677
    '''

    return 2 * math.pi * r

