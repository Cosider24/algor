class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

    def update_rating(self, new_rating):
        self.rating = new_rating

restaurant1 = Restaurant("КонсайдерБургер", "Американские бургеры", 4)
restaurant1.describe_restaurant()

restaurant1.update_rating(5)

restaurant1.describe_restaurant()
