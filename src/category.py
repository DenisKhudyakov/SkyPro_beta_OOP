from collections import Counter
class Category:

    def __init__(self, name: str, description: str, products: list) -> None:
        """конструктор класса, категория товаров, атрибуты: название, описание, перечень продуктов"""
        self.name = name
        self.description = description
        self.products = products
        self.count_category = len(list(filter(lambda prod: prod.quantity_in_stock, self.products)))
        self.count_product = len(set(self.products))



