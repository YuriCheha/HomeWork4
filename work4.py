# num = input("Введите целое число: ")
# count = [0] * 10
# for digit in num:
#     count[int(digit)] += 1
# for i in range(10):
#     print("Количество цифр", i, "в числе:", count[i])


# num = input("Введите целое число: ")
# result = ""
# for digit in num:
#     if digit == "0":
#         result += "9"
#     else:
#         result += str(9 - int(digit))
# print("Результат: ", result)

# import random
# lst = [random.randint(0,10) for i in range(5)]
#
# result = int("".join(map(str, lst)))
# print(lst)
# print(result)

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
#
# if b-a == c-b:
#     print("Числа являются последовательными элементами арифметической последовательности")
# else:
#     print("Числа не являются последовательными элементами арифметической последовательности")


# days = {
#     1: "Понедельник",
#     2: "Вторник",
#     3: "Среда",
#     4: "Четверг",
#     5: "Пятница",
#     6: "Суббота",
#     7: "Воскресенье"
# }
# num = int(input("Введите число от 1 до 7: "))
# if num in days:
#     print("День недели:", days[num])
# else:
#     print("Некорректный ввод")

# try:
#     A = float(input("Введите значение A: "))
#     B = float(input("Введите значение B: "))
#
#     if A == 0 and B == 1:
#         print("Уравнение имеет бесконечно много решений")
#     elif A == 0 or A == B + 1:
#         print("Уравнение не имеет решений")
#     else:
#         x = (B - 1) / (A - 1)
#         print(f"Решение уравнения: x = {x}")
#
# except ValueError:
#     print("Ошибка: введены некорректные значения параметров A и/или B")

# a = float(input("Введите значение a: "))
# b = float(input("Введите значение b: "))
# c = float(input("Введите значение c: "))
# try:
#     d = b ** 2 - 4 * a * c
#     if d < 0:
#         raise ValueError("Уравнение не имеет решений")
#     elif d == 0:
#         print(-b / (2 * a))
#
#     else:
#         x1 = (-b + (d**0.5)) / (2 * a)
#         x2 = (-b - (d**0.5)) / (2 * a)
#         print(x1, x2)
# except ZeroDivisionError:
#     raise ValueError("Коэффициент a не должен быть равен нулю")

# import math
#
# A = float(input("Введите значение A: "))
# if A == 0:
#     print('x = -1')
# else:
#     x = math.sin(A) / (A * (A - 1))
#     print(f"x = {x}")


# import random
#
# rows = 3
# columns = 3
# matrix = [[random.randint(0,50) for j in range(columns)] for i in range(rows)]
# for row in matrix:
#     print(row)
# max_z = 0
# for row in matrix:
#     for num in row:
#         if num > max_z:
#             max_z = num
# print("Максимальное значение:", max_z)


# import random
#
# rows = 3
# columns = 3
# matrix = [[random.randint(0,50) for j in range(columns)] for i in range(rows)]
# for row in matrix:
#     print(row)
# for i in range(3):
#     for j in range(3):
#         if matrix[i][j] % 2 == 0:
#             matrix[i][j] = 0
# for row in matrix:
#     print(row)



