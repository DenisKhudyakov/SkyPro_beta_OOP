from src.product import Product
from src.category import Category
from src.views import read_json, PATH_FILE



if __name__ == '__main__':
    prod1 = Product(name="Молоко", description="Молочные продукты", price=60, quantity_in_stock=10)
    prod2 = Product(name="Паштет", description="Мясные изделия", price=100, quantity_in_stock=15)
    prod3 = Product(name="Колбаса", description="Мясные изделия", price=300, quantity_in_stock=5)
    prod4 = Product(name="Сыр", description="Молочные продукты", price=500, quantity_in_stock=9)
    prod5 = Product(name="Сыр", description="Молочные продукты", price=500, quantity_in_stock=0)
    _list = [prod1, prod2, prod3, prod4, prod5]
    market = Category('Продуктовый', 'Маркетплэйс продуктовых товаров', _list)
    print(Category('x', 'y', _list).count_category)
    print(Category('x', 'y', _list).count_product)
    assert Category.count_category == 4
    assert Category.count_product == 5
    assert prod1.name == 'Молоко'
    assert prod4.price == 500
    assert market.name == 'Продуктовый'
    def initial_class_generator(func):
        for i in func:
            yield Category(i['name'], i['description'], [Product(y['name'], y['description'], y['price'], y['quantity']) for y in i['products']])

    print(next(initial_class_generator(read_json(PATH_FILE))))



