from string import ascii_letters, digits

from utils_customer import is_all_string_checks_valid as all_str, is_string_ascii

"""
This module stores product information
Some attributes are checked by methods from the module utils_customer
- Название +
- Описание +
- Цена +
- Оставшееся количество ????
- Для товаров в заказе хранить: название и количество. ??????
"""
ALLOWED = ascii_letters + digits + ''


class Product:
    def __init__(self, name: str, description: str, price: int):
        self.name = name
        self.description = description
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if all_str(name):
            self.__name = name
        else:
            raise ValueError(f'Only allowed in name: {ALLOWED}')

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        if len(description) > 2:
            self.__description = description
        else:
            raise ValueError(f'len address < 3')

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: int):
        if type(price) is int and price > 0:
            self.__price = price
        else:
            raise ValueError(f'only target positive numbers are allowed')


if __name__ == '__main__':
    prod1 = Product('Luk', 'prostoi, green luk', 30)
