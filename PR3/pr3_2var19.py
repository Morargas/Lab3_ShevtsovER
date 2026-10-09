import math

print("Введите координаты x и у")
x = float(input())
y = float(input())
if (y<math.pow(x,2) and y>(2-x)):
    print(f'Точка ({x},{y}) принадлежит заштрихованной области')
elif (y<math.pow(x,2) and y<(2-x)):
    print(f'Точка ({x},{y}) принадлежит заштрихованной области')
else:
    print(f'Точка ({x},{y}) не принадлежит заштрихованной области')