# num = input("Введите целое число: ")
# count = [0] * 10
# for digit in num:
#     count[int(digit)] += 1
# for i in range(10):
#     print("Количество цифр", i, "в числе:", count[i])


num = input("Введите целое число: ")
result = ""
for digit in num:
    if digit == "0":
        result += "9"
    else:
        result += str(9 - int(digit))
print("Результат: ", result)
