
import csv

itog = 0

with open("f.csv","r", encoding='utf-8') as file:
    list = csv.reader(file)
    next(list)
    for f in list:
        name = f[0]
        col = int(f[1])
        price = int(f[2])
        itog += col*price
        print(name," - ",col," шт за ",price)
print(itog)