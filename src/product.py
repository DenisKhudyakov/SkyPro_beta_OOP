from typing import Optional
from abc import ABC, abstractmethod

class ExampleProduct(ABC):
    @abstractmethod
    def add_product(self, *args):
        pass

class Product(ExampleProduct):
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

    def __str__(self) -> str:
        """Магический метод для красивого вывода класса"""
        return (
            f"Продукты {self.name} цена {self.price} остаток {self.quantity_in_stock}"
        )

    def __add__(self, other):
        """Метод получения суммарной стоимости продукта"""
        total_price = self.price * self.quantity_in_stock
        total_price += other.price * other.quantity_in_stock
        return total_price

class Smartphone(Product):
    """Класс смартфоны, отдельно существующий продукт"""
    def __init__(self, name: str, description: str, price: float, quantity_in_stock: int, efficiency: float, model: str, memory: int, color: str) -> None:
        """Расширение дочернего класса, дополнены параметры: производительность, модель, объем памяти, цвет"""
        super().__init__(name, description, price, quantity_in_stock)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if isinstance(other, Smartphone):
            return self.price + other.price
        raise TypeError

    @classmethod
    def add_product(cls, *args) -> None:
        """Задание №3 доработка функции добавления продуктов в каталог"""
        if issubclass(cls, Product):
            cls.product_list.append(cls(*args))

class LawnGrass(Product):
    """Класс трава газонная, отдельно существующий продукт"""
    def __init__(self, name: str, description: str, price: float, quantity_in_stock: int, country: str, germination_period: str, color: str) -> None:
        """Расширение дочернего класса, дополнены параметры: страна производитель, период прорастания, цвет"""
        super().__init__(name, description, price, quantity_in_stock)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if isinstance(other, LawnGrass):
            return self.price + other.price
        raise TypeError

    @classmethod
    def add_product(cls, *args) -> None:
        """Задание №3 доработка функции добавления продуктов в каталог"""
        if issubclass(cls, Product):
            cls.product_list.append(cls(*args))


if __name__ == '__main__':
    prod1 = Product(name="Молоко", description="Молочные продукты", price=60, quantity_in_stock=10)
    prod2 = Smartphone('Nokia', 'Any smartphone', 10000, 10, 5000.00, 'zf-1000', 3000, 'red')
    prod4 = Smartphone('Nokia2', 'Any smartphone', 15000, 10, 5000.00, 'zf-1000', 3000, 'red')
    prod3 = LawnGrass('Овсянница', 'Широко распространенное растение', 100.50, 10000, 'Russia', '3 month', 'green')
    print(type(prod1))
    print(type(prod2))
    print(isinstance(type(prod2), type(prod1)))
    print(prod2 + prod4)
    prod2.add_product('Nokia2', 'Any smartphone', 15000, 10, 5000.00, 'zf-1000', 3000, 'red')
    print(prod2.product_list)
