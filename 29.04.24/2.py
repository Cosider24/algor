def nom2():
    party = {
        "НГ" : "year.jpg",
        "8 марта":"mart.jpg",
        "23 февраля":"feb.jpg"
    }
    x = input("введите праздник: ")
    for key in party:
        if key == x:
            print("Открытка загружается")
            y = Image.open(party[key])
            y.show()