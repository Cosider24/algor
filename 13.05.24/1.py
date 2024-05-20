import json

with open('products.json', 'r') as f:
    products = json.load(f)

for product in products['products']:
    print(f'Название: {product["name"]}')
    print(f'Цена: {product["price"]}')
    print(f'Вес: {product["weight"]}')
    if product['available']:
        print('В наличии')
    else:
        print('Нет в наличии!')
    print()

