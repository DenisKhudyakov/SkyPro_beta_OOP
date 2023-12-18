from src.product import Product
from src.category import Category



if __name__ == '__main__':
    prod1 = Product(name="Молоко", description="Молочные продукты", price=60, quantity_in_stock=10)
    prod2 = Product(name="Паштет", description="Мясные изделия", price=100, quantity_in_stock=15)
    prod3 = Product(name="Колбаса", description="Мясные изделия", price=300, quantity_in_stock=5)
    prod4 = Product(name="Сыр", description="Молочные продукты", price=500, quantity_in_stock=9)
    _list = [prod1, prod2, prod3, prod4]
    market = Category('Продуктовый', 'Маркетплэйс продуктовых товаров', _list)
    assert market.count_category == 4
    assert market.count_product == 4
    assert prod1.name == 'Молоко'
    assert prod4.price == 500
    assert market.name == 'Продуктовый'



