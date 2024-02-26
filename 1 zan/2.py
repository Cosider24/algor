nom = int(input ())
if nom % 2 == 0 and nom >= 1 and nom <=36:
    print ("Купе Верхнее")
elif nom % 2 == 1 and nom >= 1 and nom <=36:
    print ("Купе нижнее")
elif nom % 2 == 0 and nom >= 37 and nom <= 53:
    print ("Боковое Верхнее")
elif nom % 2 == 1 and nom >= 37 and nom <= 53:
    print ("Боковое нижнее")
else:
    print("Ошибка")