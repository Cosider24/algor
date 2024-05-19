import json

with open('products.json', 'r') as f:
    products = json.load(f)

new_product = {}
new_product["name"] = input("Введите название продукта: ")
new_product["price"] = int(input("Введите цену продукта: "))
new_product["weight"] = int(input("Введите вес продукта: "))
new_product["available"] = input("Доступен ли продукт? (да/нет): ") == "да"

products.append(new_product)

with open('products.json', 'w') as f:
    json.dump(products, f)

for product in products:
    print("Название:", product["name"])
    print("Цена:", product["price"])
    print("Вес:", product["weight"])
    if product["available"]:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print()
