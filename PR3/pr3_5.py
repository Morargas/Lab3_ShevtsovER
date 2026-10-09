try:
    print("Введите число")
    number = int(input())
    if number % 2 == 1:
        print(f'Число {number} - нечетное')
    else:
        print(f'Число {number} - четное')
except ValueError:
    print("Некорректный тип данных.")