class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        super().__init__(restaurant_name, cuisine_type, rating)
        self.flavors = []

    def display_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print(f"- {flavor}")

ice_cream_stand = IceCreamStand("Sweet Spot", "Ice Cream", 4)

ice_cream_stand.flavors = ["Ванильное", "Шоколадное", "Клубничное"]

ice_cream_stand.display_flavors()
