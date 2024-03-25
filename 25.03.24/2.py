numbers = [1,2,3,4,5,1,2,3]
pov = []
nepov = {}
for n in numbers:
    if n in nepov:
        pov.append(n)
    else:
        nepov[n] = True
if pov:
    print("Повторяющиеся элементы в списке:", pov)
else:
    print("Нет повторяющихся элементов в списке")