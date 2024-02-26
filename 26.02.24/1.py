words = []
N = int(input("Введите количество слов"))
for i in range (N):
    word = input("Введите слово: ")
    words.append(word)
res = ''.join(words)
print("Результат", res)
