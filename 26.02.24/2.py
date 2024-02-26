words = []
word = input("Введите слово")
while word != "стоп":
    word = input("Введите слово: ")
    words.append(word)
res = ''.join(words)
print("Результат", res)