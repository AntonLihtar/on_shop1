"""The module stores validators for entities.product"""


def validator_description(value: str):
    if len(value) < 3:
        raise ValueError(f'len address < 3')


def validator_price(value: int):
    if not (type(value) is int and value > 0):
        raise ValueError(f'only target positive numbers are allowed')
