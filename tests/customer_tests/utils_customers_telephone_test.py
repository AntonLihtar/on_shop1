import pytest

from entities.utils_customer import is_correct_telephone


def test_validate():
    is_correct_telephone('+79991231234')


def test_validate2():
    is_correct_telephone('89991231234')


def test_telephone_chars():
    with pytest.raises(ValueError) as e:
        is_correct_telephone('+792312345677')
    assert 'Invalid number only allowed +79991112222 or 89991112222' == e.value.args[0]


def test_telephone_chars2():
    with pytest.raises(ValueError) as e:
        is_correct_telephone('+792312345')
    assert 'Invalid number only allowed +79991112222 or 89991112222' == e.value.args[0]


def test_telephone_chars3():
    with pytest.raises(ValueError) as e:
        is_correct_telephone('+7999123123+')
    assert 'Invalid number only allowed +79991112222 or 89991112222' == e.value.args[0]


def test_telephone_chars4():
    with pytest.raises(ValueError) as e:
        is_correct_telephone('+ghy91231234')
    assert 'Invalid number only allowed +79991112222 or 89991112222' == e.value.args[0]


def test_telephone_chars5():
    with pytest.raises(ValueError) as e:
        is_correct_telephone('+fghjnbytvre')
    assert 'Invalid number only allowed +79991112222 or 89991112222' == e.value.args[0]


def test_telephone_chars6():
    with pytest.raises(ValueError) as e:
        is_correct_telephone('+72')
    assert 'Invalid number only allowed +79991112222 or 89991112222' == e.value.args[0]


def test_telephone_chars7():
    with pytest.raises(ValueError) as e:
        is_correct_telephone('')
    assert 'Invalid number only allowed +79991112222 or 89991112222' == e.value.args[0]


def test_telephone_chars8():
    with pytest.raises(ValueError) as e:
        is_correct_telephone('8_991114444')
    assert 'Invalid number only allowed +79991112222 or 89991112222' == e.value.args[0]


if __name__ == '__main__':
    pytest.main()
