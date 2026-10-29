import math
import os
import random
import time
from fractions import Fraction
def calculator():
    a = 0
    while a < 100:
        print(f"Загрузка: {a}%", end="\r")
        time.sleep(random.randint(1, 10))
        a += random.randint(0, 99)

        if a == 100:
            print("plug")
            break

    print(f"Загрузка: 100%")
    time.sleep(1)
    print('@'*8, ' '*4, '@'*8, ' '*5, '@'*3, ' '*10, '@'*1, ' '*1, '@'*8, ' '*2, '@'*7)
    time.sleep(0.1)
    print(' '*7, '@'*1, ' '*3, '@'*1, ' '*11, '@'*1, ' '*1, '@'*1, ' '*8, '@'*1, ' '*5, '@'*1, ' '*5, '@'*1)
    time.sleep(0.1)
    print(' '*7, '@'*1, ' '*3, '@'*1, ' '*11, '@'*1, ' '*1, '@'*1, ' '*7, '@'*1, ' '*6, '@'*1, ' '*5, '@'*1)
    time.sleep(0.1)
    print('@'*8, ' '*4, '@'*1, '', '@'*5, ' '*3, '@'*1, ' '*3,  '@'*1, ' '*5, '@'*1, ' '*7,  '@'*1, ' '*6,  '@'*7)
    time.sleep(0.1)
    print(''*1, '@'*1, ' '*10, '@'*1, ' '*10, '@'*1,  ' '*3, '@'*1, ' '*4, '@'*1, ' '*8, '@'*1, ' '*12, '@'*1)
    time.sleep(0.1)
    print(' '*2, '@'*1, ' '*8, '@'*1, ' '*9, '@'*1, ' '*5, '@'*1, ' '*2, '@'*1, ' '*9, '@'*1, ' '*12, '@'*1)
    time.sleep(0.1)
    print(' '*4, '@'*1, ' '*6, '@'*8, ' '*2, '@'*1, ' '*5, '@'*1, ' '*2, '@'*7, ' '*1, '@'*6, ' '*3,  '@'*7)
    time.sleep(0.1)
    print("Добро пожаловать в 'Realis'!")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Realis: Консольное издание. Версия 2.0.\nРазработано Orion3718.")
    print("Помощь: e = 2.718281828459045")
    print("Доступные разделы: числовые операции, операции с дробями")
    time.sleep(1)
    while True:
        action = input("Выберите раздел: ")
        if action == 'числовые операции':
            try:         
                operation = input("Выберите операцию: ")
                if operation == '+':
                    a = float(input("Первое слагаемое: "))
                    b = float(input("Второе слагаемое: "))
                elif operation == '-':
                    a = float(input("Уменьшаемое: "))
                    b = float(input("Вычитаемое: "))
                elif operation == '*':
                    a = float(input("Множимое: "))
                    b = float(input("Множитель: "))
                elif operation == '/':
                    print("Виды деления:\n1. Стандартное\n2. Целочисленное")
                    division_type = input("Выберите вид деления: ")
                    if division_type == '1':
                        a = float(input("Делимое: "))
                        b = float(input("Делитель: "))
                    elif division_type == '2':
                        a = float(input("Делимое: "))
                        b = float(input("Делитель: "))
                    else:
                        print("Ошибка: Выбранного вида не существует!")
                elif operation == '^':
                    a = float(input("Основание степени: "))
                    b = float(input("Показатель степени: "))
                elif operation == '√':
                    a = float(input("Подкоренное выражение: "))
                    b = float(input("Показатель степени корня: "))
                elif operation == '|a|':
                    a = float(input("Число: "))
                elif operation == 'a!':
                    a = int(input("Число: "))
                elif operation == 'log':
                    a = float(input("Аргумент логарифма: "))
                    b = float(input("Основание логарифма: "))
                elif (operation == 'lg') or (operation == 'ln'):
                    a = float(input("Аргумент логарифма: "))
                elif (operation == 'sin') or (operation == 'cos') or (operation == 'tg') or (operation == 'ctg') or (operation == 'sec') or (operation == 'cosec'):
                    angle_degrees = float(input("Введите градусную меру угла: "))
                    angle_radians = math.radians(angle_degrees)
                elif (operation == 'arcsin') or (operation == 'arccos') or (operation == 'arctg'):
                    number = float(input("Введите значение основной функции: "))
                elif operation == "назад":
                    continue
            except ValueError:
                print(f"Ошибка: Отсутствует одно или несколько чисел!")
                continue

            if operation == '+':
                result = a + b
                print(f"Сумма: {result}")
            elif operation == '-':
                result = a - b
                print(f"Разность: {result}")
            elif operation == '*':
                result = a * b
                print(f"Произведение: {result}")
            elif operation == '/':
                if division_type == '1':
                    if b != 0:
                        result = a / b
                        print(f"Частное: {result}")
                    else:
                        print(f"Ошибка: Деление на ноль не определено!")
                        continue
                elif division_type == '2':
                    if b != 0:
                        result = a // b
                        remainder = a % b
                        print(f"Частное: {result},\nОстаток: {remainder}")
                    else:
                        print(f"Ошибка: Деление на ноль не определено!")
                        continue
            elif operation == '^':
                result = a ** b
                print(f"Степень: {result}")
            elif operation == '√':
                if (a < 0) and (b % 2 == 0):
                    print("Ошибка: Подкоренное выражение не должно быть меньше нуля!")
                elif (a < 0) and (b % 2 == 1):
                    result = -((-a) ** (1 / b))
                    print(f"Основание: {result}")
                else:
                    result = a ** (1 / b)
                    print(f"Основание: {result}")
            elif operation == '|a|':
                result = abs(a)
                print(f"Модуль числа: {result}")
            elif operation == 'a!':
                result = math.factorial(a)
                print(f"Факториал числа: {result}")
            elif operation == 'log':
                if (a > 0) and (b > 1):
                    result = math.log(a, b)
                    print(f"Логарифм: {result}")
                else:
                    print("Ошибка: Аргумент и основание логарифма должны быть больше нуля и не равны единице!")
            elif operation == 'lg':
                if (a > 0) and (b > 1):
                    result = math.log10(a)
                    print(f"Логарифм: {result}")
                else:
                    print("Ошибка: Аргумент и основание логарифма должны быть больше нуля и не равны единице!")
            elif operation == 'ln':
                if (a > 0) and (b > 1):
                    result = math.log(a)
                    print(f"Логарифм: {result}")
                else:
                    print("Ошибка: Аргумент и основание логарифма должны быть больше нуля и не равны единице!")
            elif operation == 'sin':
                if (angle_degrees == 0) or (angle_degrees == 180) or (angle_degrees == 360):
                    print(f"Синус угла: 0.0")
                else:
                    result = math.sin(angle_radians)
                    print(f"Синус угла: {result}")
            elif operation == 'cos':
                if (angle_degrees == 90) or (angle_degrees == 270):
                    print(f"Косинус угла: 0.0")
                else:
                    result = math.cos(angle_radians)
                    print(f"Косинус угла: {result}")
            elif operation == 'tg':
                if (angle_degrees == 90) or (angle_degrees == 270):
                    print(f"Ошибка: Для данного угла тангенс не определён!")
                elif (angle_degrees == 0) or (angle_degrees == 180) or (angle_degrees == 360):
                    print(f"Тангенс угла: 0.0")
                else:
                    result = math.tan(angle_radians)
                    print(f"Тангенс угла: {result}")
            elif operation == 'ctg':
                if (angle_degrees == 0) or (angle_degrees == 180) or (angle_degrees == 360):
                    print(f"Ошибка: Для данного угла котангенс не определён!")
                elif (angle_degrees == 90) or (angle_degrees == 270):
                    print(f"Котангенс угла: 0.0")
                else:
                    result = (math.cos(angle_radians))/(math.sin(angle_radians))
                    print(f"Котангенс угла: {result}")
            elif operation == 'arcsin':
                if (-1 <= number <= 1):
                    angle_radians = math.asin(number)
                    result = math.degrees(angle_radians)
                    print(f"Арксинус угла: {result}")
                else:
                    print(f"Ошибка: Входное значение должно лежать в промежутке [-1;1]")
            elif operation == 'arccos':
                if (-1 <= number <= 1):
                    angle_radians = math.acos(number)
                    result = math.degrees(angle_radians)
                    print(f"Арккосинус угла: {result}")
                else:
                    print(f"Ошибка: Входное значение должно лежать в промежутке [-1;1]")
            elif operation == 'arctg':
                angle_radians = math.atan(number)
                result = math.degrees(angle_radians)
                print(f"Арктангенс угла: {result}")
            elif operation == 'sec':
                if (angle_degrees == 90) or (angle_degrees == 270):
                    print(f"Ошибка: Для данного угла секанс не определён!")
                else:
                    result = 1/math.cos(angle_radians)
                    print(f"Секанс угла: {result}")
            elif operation == 'cosec':
                if (angle_degrees == 0) or (angle_degrees == 180) or (angle_degrees == 360):
                    print(f"Ошибка: Для данного угла косеканс не определён!")
                else:
                    result = 1/math.sin(angle_radians)
                    print(f"Косеканс угла: {result}")
            else:
                print("Ошибка: Недоступная команда!")

        elif action == 'операции с дробями':
            try:
                print("Доступные операции: +, -")
                operation = input("Выберите операцию: ")
                if operation == '+':
                    a = Fraction(input("Первое слагаемое: "))
                    b = Fraction(input("Второе слагаемое: "))
                elif operation == '-':
                    a = Fraction(input("Уменьшаемое: "))
                    b = Fraction(input("Вычитаемое: "))
                elif operation == "назад":
                    continue
            except ZeroDivisionError:
                print(f"Ошибка: Знаменатель дроби должен быть больше нуля!")
                continue
            except ValueError:
                print(f"Ошибка: Отсутствует одно или несколько чисел!")
                continue

            if operation == '+':
                result = a + b
                print(f"Сумма: {result}")
            elif operation == '-':
                result = a - b
                print(f"Разность: {result}")
            else:
                print("Ошибка: Недоступная команда!")
calculator()