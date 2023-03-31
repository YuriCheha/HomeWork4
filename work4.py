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


days = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье"
}
num = int(input("Введите число от 1 до 7: "))
if num in days:
    print("День недели:", days[num])
else:
    print("Некорректный ввод")