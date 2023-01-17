from string import ascii_letters, digits

from utils_customer import validate_all_string_checks as all_str
from utils_product import validator_description as v_des, validator_price as v_pr

"""
This module stores product information
Some attributes are checked by methods from the module utils_customer

- Оставшееся количество ????
- Для товаров в заказе хранить: название и количество. ??????
"""
ALLOWED = ascii_letters + digits + ' _-'


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
        all_str(name, ALLOWED)
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        v_des(description)
        self.__description = description

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: int):
        v_pr(price)
        self.__price = price


if __name__ == '__main__':
    prod1 = Product('Luk', 'prostoi, green luk', 30)
    prod2 = Product('yuk_ 1', 'prostoi_ *StEp* green luk', 500)
    prod3 = Product('kir1-1', 'prostoi, green // test // luk', 3000)
