import json

with open('products.json') as f:
    products = json.load(f)

for product in products:
    print("Название:", product["name"])
    print("Цена:", product["price"])
    print("Вес:", product["weight"])
    if product["available"]:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print()
