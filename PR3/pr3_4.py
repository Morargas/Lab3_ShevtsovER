try:
    print("введите год")
    year = int(input())
    if year % 4 == 0:
        print("Год является високосным")
    else:
        print("Год не является високосным")
except ValueError:
    print("Неверный тип данных")