import pytest

from entities.utils_product import validator_description


def test_len_string():
    validator_description('Salut 123')


def test_len_string2():
    with pytest.raises(ValueError) as e:
        validator_description('')
    assert 'len address < 3' == e.value.args[0]


def test_len_string3():
    with pytest.raises(ValueError) as e:
        validator_description('**')
    assert 'len address < 3' == e.value.args[0]


def test_type_string1():
    with pytest.raises(TypeError) as e:
        validator_description([1, 2, 3, 4])
    assert 'wrong type, needed str' == e.value.args[0]


def test_type_string2():
    with pytest.raises(TypeError) as e:
        validator_description({1: 'sds', 2: 'sdd2', 3: 'ffff', 4: 'sdsd11'})
    assert 'wrong type, needed str' == e.value.args[0]


def test_type_string3():
    with pytest.raises(TypeError) as e:
        validator_description(12345)
    assert 'wrong type, needed str' == e.value.args[0]


if __name__ == '__main__':
    pytest.main()
