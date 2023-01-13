"""
This module stores product information
- Название +
- Описание +
- Цена +
- Оставшееся количество ????
- Для товаров в заказе хранить: название и количество. ??????
"""


class Product:
    def __init__(self, name: str, specification: str, price: int):
        self.name = name
        self.specification = specification
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: int):
        self.__price = price
