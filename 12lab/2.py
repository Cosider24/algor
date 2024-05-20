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
    def __init__(self, restaurant_name, cuisine_type, rating=0, location=None, hours=None):
        super().__init__(restaurant_name, cuisine_type, rating)
        self.flavors = []
        self.location = location
        self.hours = hours

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)

    def has_flavor(self, flavor):
        return flavor in self.flavors

    def display_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print(f"- {flavor}")

ice_cream_stand = IceCreamStand("Sweet Spot", "Ice Cream", 4, "ул. Ленина, д. 10", "10:00 - 22:00")

ice_cream_stand.add_flavor("Ванильное")
ice_cream_stand.add_flavor("Шоколадное")
ice_cream_stand.add_flavor("Клубничное")

ice_cream_stand.remove_flavor("Клубничное")

print(ice_cream_stand.has_flavor("Ванильное"))
print(ice_cream_stand.has_flavor("Клубничное"))

ice_cream_stand.display_flavors()
