numbers = [3, 7, 12, 5, 9]
num = int(input("введите число"))
if num in numbers:
    print("Вы угадали число!")
else:
    print("В списке нет такого числа")
print("Исходный список чисел:", numbers)
print("Число пользователя", num)