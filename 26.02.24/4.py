import random

errors = 0
correct_answer = 0

while errors < 3:
    a = int(random.random() * 10)
    b = int(random.random() * 10)
    correct_choice = str(a) + "+" + str(b) + "="
    print(correct_choice, end = " ")
    user_answer = int(input())
    if user_answer == (a + b):
        print("True")
        correct_answer+= 1
    else:
        print("False")
        errors += 1
print("Игра окончена! Правильных ответов: ", correct_answer)