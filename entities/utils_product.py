"""The module stores validators for entities.product"""


def validator_description(value: str):
    if type(value) != str:
        raise TypeError('wrong type, needed str')
    if len(value) < 3:
        raise ValueError(f'len address < 3')


def validator_price(value: int):
    if type(value) != int:
        raise TypeError('wrong type, needed int')
    if value < 1:
        raise ValueError(f'only target positive numbers are allowed')
