
def squareFigures(figures,h,l,r):
    match figures:
        case 'Квадрат': return print(f'Площадь квадрата составит: {h**2}.')
        case 'Круг': return print(f'Площадь круга составит: {3,14 * (r**2)}.') 
        case 'Прямоугольник': return print(f'Площадь прямоугольника составит: {h*l }.')
        case 'Треугольник': return print(f'Площадь треугольника составит: {1/2 *l*h}.')