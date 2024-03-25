dney = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
vxd = int(input("сколько выходных вы хотите?"))
if vxd >= len(dney):
    ptint ("ошибка, в неделе всего 7 дней!")
else:
    rab = len(dney) - vxd
    vxdney = dney[-vxd:]
    rabdney = dney[:-vxd]

    print("выходные дни: ", ", ".join(vxdney))
    print("рабочих дней: ", ", ".join(rabdney))