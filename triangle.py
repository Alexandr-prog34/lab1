def area(a, h):
    '''
    Принимает сторону треугольника и высоту опущенную к ней, возврашает площадь треугольника.

        Параметры:
            a (int): сторона треугольника
            h (int): высота треугольника, опущенная к стороне a

        Возвращаемое значение:
            a * h / 2 (float): площадь треугольника со стороной a и опущенной к ней высоте h

        Примеры использования:
            Входные данные:
                a = 4
                h = 3
            Выходные данные:
                area = 6.0
    '''
    if type(a) != int or type(h) != int:
        return TypeError
    if a < 0 or h < 0:
        return ValueError
    return a * h / 2

def perimeter(a, b, c):
    '''
    Принимает стороны треугольника, возврашает периметр треугольника.

        Параметры:
            a (int): сторона треугольника
            b (int): сторона треугольника
            c (int): сторона треугольника

        Возвращаемое значение:
            a + b + c (int): периметр треугольника со сторонами a,b и c

        Примеры использования:
            Входные данные:
                a = 3
                b = 4
                c = 5
            Выходные данные:
                perimeter = 12
    '''
    if type(a) != int or type(b) != int or type(c) != int:
        return TypeError
    if a < 0 or b < 0 or c < 0:
        return ValueError
    return a + b + c
