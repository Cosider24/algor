from PIL import Image

def nom2(party):
    x = input("Введите праздник: ")
    for key in party:
        if key == x:
            print("Открытка загружается")
            y = Image.open(party[key])
            y.show()

party = {
    "Новый Год" : "newyear.jpg",
    "8 марта":"march.jpg",
    "23 февраля":"feb.jpg"
}

nom2(party)