try:
    print("Введите свой рост и вес")
    height = int(input())
    weight = int(input())
    if height - 100 > weight:
        print("Рекомендуется набрать вес")
    elif height - 100 == weight:
        print("у вас оптимальный вес")
    else:
        print("Рекомендуетмя сбросить вес")
except ValueError:
    print("Неверный тип данных")