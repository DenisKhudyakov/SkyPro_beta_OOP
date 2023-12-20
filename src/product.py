from typing import Optional


class Product:
    product_list: list = []

    def __init__(
        self, name: str, description: str, price: float, quantity_in_stock: int
    ) -> None:
        """конструктор класса продукт, атрибуты название, описание, цена, количество вналичии"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    @property
    def get_price(self) -> float:
        return self.price

    @get_price.setter
    def get_price(self, new_price: float):
        if new_price < self.price:
            message = input("Подтвердите сниженеи цены Y - Да, N - Нет ").lower()
            if message == "y":
                self.price = new_price
                return
        self.price = new_price

    @property
    def get_product(self):
        """Получаем данные о продукте"""
        return f"Продукт, {self.price} руб. Остаток: {self.quantity_in_stock} шт."

    @classmethod
    def init_product(
        cls, name: str, description: str, price: float, quantity_in_stock: int
    ) -> Optional:
        """Инициализация класса"""
        return cls(name, description, price, quantity_in_stock)

    @classmethod
    def add_product(
        cls, name: str, description: str, price: float, quantity_in_stock: int
    ) -> None:
        """Добавление экземпляров класса в список"""
        cls.product_list.append(
            cls.init_product(name, description, price, quantity_in_stock)
        )

    def __repr__(self) -> str:
        """Магический метод для красивого вывода класса"""
        return (
            f"Продукты {self.name} цена {self.price} остаток {self.quantity_in_stock}"
        )
