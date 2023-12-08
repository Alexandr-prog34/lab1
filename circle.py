import math


def area(r):
	'''
	Функция получает на вход длину радиуса круга и возвращает значение его площади.
	Например:
	Ввод: 7
	Вывод: 153.93804... 
	'''
    return math.pi * r * r


def perimeter(r):
	'''
	Функция получает на вход длину радиуса круга и возвращает значение его периметра.
	Например:
	Ввод: 7
	Вывод: 43.9823... 
	'''
    return 2 * math.pi * r

