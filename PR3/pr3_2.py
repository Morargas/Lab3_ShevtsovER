try:
    print("введите длины сторон треугольника")
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    if n1 == n2 == n3:
        print("Треугольник - равносторонний")
    elif n1 == n2 or n2 == n3 or n3 == n1:
        print("Треугольник - равнобедренный")
    else:
        print("Треугольник - разносторонний")
except ValueError:
    print("Некорректный тип данных.")