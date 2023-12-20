from collections import Counter


class Category:
    count_category: int = 0
    count_product: int = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """конструктор класса, категория товаров, атрибуты: название, описание, перечень продуктов"""
        self.name = name
        self.description = description
        self.__products = products
        Category.count_category = len(
            list(filter(lambda prod: prod.quantity_in_stock, self.__products))
        )
        Category.count_product = len(set(self.__products))

    @property
    def get_products(self):
        for i_prod in self.__products:
            yield f'Продукт, {i_prod.price} руб. Остаток: {i_prod.quantity_in_stock} шт.'
