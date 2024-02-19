cvet = input ()
cvet1 = input ()
if (cvet == "красный" and cvet1 == "синий") or (cvet == "синий" and cvet1 == "красный"):
    print("фиолетовый")
elif (cvet == "красный" and cvet1 == "желтый") or (cvet == "желтый" and cvet1 == "красный"):
    print("оранжевый")
elif (cvet == "синий " and cvet1 == "желтый") or (cvet == "желтый" and cvet1 == "синий "):
    print("зеленый")
else:
    print("Ошибка")