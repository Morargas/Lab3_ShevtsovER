try:
    print("Введите три числа")
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    count = 1
    while n1 // count >= 1:
        
        count = count * 10
except ValueError:
    print("Неверный тип данных")