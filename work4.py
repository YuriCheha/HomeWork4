num = input("Введите целое число: ")
count = [0] * 10
if num.isdigit():
    for digit in num:
        count[int(digit)] += 1

    for i in range(10):
        print("Количество цифр", i, "в числе:", count[i])
else:
    print('Число должно быть типа int')