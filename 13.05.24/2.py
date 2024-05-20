import json

with open('products.json', 'r') as f:
    products = json.load(f)

new_product = {}
new_product['name'] = input('Введите название продукта: ')
new_product['price'] = int(input('Введите цену продукта: '))
new_product['available'] = input('В наличии (True/False): ') == 'True'
new_product['weight'] = int(input('Введите вес продукта (г): '))
products['products'].append(new_product)

for product in products['products']:
    print(f'Название: {product["name"]}')
    print(f'Цена: {product["price"]}')
    print(f'Вес: {product["weight"]}')
    if product['available']:
        print('В наличии')
    else:
        print('Нет в наличии!')
    print()
