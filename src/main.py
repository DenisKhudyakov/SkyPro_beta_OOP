from src.category import Category
from src.product import Product
from src.views import PATH_FILE, read_json

if __name__ == "__main__":
    Product.add_product(
        name="Молоко", description="Молочные продукты", price=60, quantity_in_stock=10
    )
    Product.add_product(
        name="Паштет", description="Мясные изделия", price=100, quantity_in_stock=15
    )
    Product.add_product(
        name="Колбаса", description="Мясные изделия", price=300, quantity_in_stock=5
    )
    Product.add_product(
        name="Сыр", description="Молочные продукты", price=500, quantity_in_stock=9
    )
    Product.add_product(
        name="Сыр", description="Молочные продукты", price=500, quantity_in_stock=1
    )
    for i in Product.product_list:
        print(i)
    print(
        Product.init_product(
            name="Молоко",
            description="Молочные продукты",
            price=60,
            quantity_in_stock=10,
        )
    )

    prod1 = Product(
        name="Молоко", description="Молочные продукты", price=60, quantity_in_stock=10
    )
    print(prod1.get_price)
    prod1.get_price = 30
    print(prod1.get_price)

    # _list = [prod1, prod2, prod3, prod4, prod5]
    # market = Category('Продуктовый', 'Маркетплэйс продуктовых товаров', _list)
    # print(Category('x', 'y', _list).count_category)
    # print(Category('x', 'y', _list).count_product)
    # assert Category.count_category == 4
    # assert Category.count_product == 5
    # assert prod1.name == 'Молоко'
    # assert prod4.price == 500
    # assert market.name == 'Продуктовый'
    # def initial_class_generator(func):
    #     for i in func:
    #         yield Category(i['name'], i['description'], [Product(y['name'], y['description'], y['price'], y['quantity']) for y in i['products']])
    #
    # print(next(initial_class_generator(read_json(PATH_FILE))))
