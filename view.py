def menu():
    print('Добро пожаловать в программу рисования линии и круга!')
    print('Введите номер опции,которой хотите воспользоваться')
    print('1. Нарисовать линию')
    print('2. Нарисовать круг')
    print('3. Завершить работу')
    number_menu = int(input('пункт меню = '))
    while(number_menu > 3 or number_menu < 1):
        print('введите корректное значение функции меню')
        number_menu = int(input('N = '))
    return number_menu


# ------------- метод для ввода координат начала и конца отрезка -------------
def coordinate():
    x1 = float(input("введите координату Х первой точки от 0 до 500 "))
    y1 = float(input("введите координату Y первой точки от 0 до 300 "))
    x2 = float(input("введите координату Х второй точки от 0 до 500 "))
    y2 = float(input("введите координату y второй точки от 0 до 300 "))
    point = [x1, y1, x2, y2]
    return point

# ------------- метод для ввода координат эллипса -------------
def coordinate_ellips():
    x1 = float(input("введите первую координату эллипса от 0 до 500 "))
    y1 = float(input("введите вторую координату эллипса от 0 до 300 "))
    x2 = float(input("введите третью координату эллипса от 0 до 500 "))
    y2 = float(input("введите четвёртую координату эллипса от 0 до 300 "))
    point = [x1, y1, x2, y2]
    return point
# -----------метод, выводящий в консоль то, что необходимо напечатать---------------------
def data_print(data):
    return print(data)