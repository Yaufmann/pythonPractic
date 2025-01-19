from math import pi

def squareFigures(figures,h=None,l=None,r=None):
    match figures:
        case 'Квадрат': return print(f'Площадь квадрата составит: {h**2}.')
        case 'Круг':
            square = r**2 * pi
            rad = round(square,2)
            return print(f'Площадь круга составит: {rad}.') 
        case 'Прямоугольник': return print(f'Площадь прямоугольника составит: {h*l}.')
        case 'Треугольник': return print(f'Площадь треугольника составит: {1/2 *l*h}.')


while True:
    print("1. Площадь квадрата")
    print("2. Площадь круга")
    print("3. Площадь прямоугольника")
    print("4. Площадь треугольника")
    print("0. выйти из программы")
    cmd = input("Выберите пункт: ")
    
    
    if cmd == "1":
        h = int(input('Введите сторону квадрата: '))
        squareFigures('Квадрат', h)
    elif cmd == "2":
        r = int(input('Введите радиус круга: '))
        squareFigures('Круг',None,None,r)
    elif cmd == "3":
        h = int(input('Введите высоту прямоугольника: '))
        l = int(input('Введите длину прямоугольника: '))
        squareFigures('Прямоугольник',h,l)
    elif cmd == "4":
        h = int(input('Введите высоту треугольника: '))
        l = int(input('Введите длину основания треугольника: '))
        squareFigures('Треугольник',h,l)
    elif cmd == "0":
        break
    else:
        print("Вы ввели неправильное значение")

