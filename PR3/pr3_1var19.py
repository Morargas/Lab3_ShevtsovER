import math

try:
    print("Введите радиус внешней и внутренней окружности (r1 и r2)")
    r1 = float(input())
    r2 = float(input())
    if r1 > r2:
        S = math.pi*(math.pow(r1,2)-math.pow(r2,2))
    elif r1 < r2:
        S = math.pi*(math.pow(r2,2)-math.pow(r1,2))
    else:
        print("Неправильные данные")
    print(f'Площадь кольца равна: {S}')
except ValueError:
    print("Неверный тип данных")