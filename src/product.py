class Product:
    def __init__(self, name: str, description: str, price: float, quantity_in_stock: int) -> None:
        """конструктор класса продукт, атрибуты название, описание, цена, количество вналичии"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock