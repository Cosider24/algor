def f(q):
    if ((q % 4 == 0) and (q % 100 != 0)) or (q % 400 == 0):
        return True
    else:
        return False
year = int(input())
if f(year) == True:
    print(year,"Год","Високосный")
else:
    print(year,"Год","Не високосный")
