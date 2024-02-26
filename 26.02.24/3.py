word = []
while not "ф" in word:
    word = input("Введите слово: ")
    if "ф" in word:
        print("Редкое слово!")
    else:
        print("Не редкое слово!")