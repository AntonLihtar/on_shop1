import pytest

from entities.utils_product import validator_price


def test_norm_price():
    validator_price(11)


def test_type_price():
    with pytest.raises(TypeError) as e:
        validator_price('1')
    assert 'wrong type, needed int' == e.value.args[0]


def test_type_price2():
    with pytest.raises(TypeError) as e:
        validator_price((1, 2, 3))
    assert 'wrong type, needed int' == e.value.args[0]


def test_type_price3():
    with pytest.raises(TypeError) as e:
        validator_price(True)
    assert 'wrong type, needed int' == e.value.args[0]


def test_value_price1():
    with pytest.raises(ValueError) as e:
        validator_price(-11)
    assert 'only target positive numbers are allowed' == e.value.args[0]


def test_value_price2():
    with pytest.raises(ValueError) as e:
        validator_price(0)
    assert 'only target positive numbers are allowed' == e.value.args[0]


if __name__ == '__main__':
    pytest.main()
