from string import ascii_letters, digits
import pytest
from entities.utils_customer import is_standard_email, is_correct_chars_email, is_2unsuitable_chars_email

ALLOWED = ascii_letters + digits
EMAIL_ALLOWED = ascii_letters + digits + '.@_-'


def test_valid_email():
    is_standard_email('test@example.com', ALLOWED)


def test_email_validate1():
    with pytest.raises(ValueError) as e:
        is_standard_email('ss@h@rr.ru', ALLOWED)
    assert 'must contain 1= @ in the middle and \'.\' in the second part, after @ and at least one character after' == \
           e.value.args[0]


def test_email_validate2():
    with pytest.raises(ValueError) as e:
        is_standard_email('test@examplecom', ALLOWED)
    assert 'must contain 1= @ in the middle and \'.\' in the second part, after @ and at least one character after' == \
           e.value.args[0]


def test_email_validate3():
    with pytest.raises(ValueError) as e:
        is_standard_email('testexample.co@m', ALLOWED)
    assert 'must contain 1= @ in the middle and \'.\' in the second part, after @ and at least one character after' == \
           e.value.args[0]


def test_email_validate4():
    with pytest.raises(ValueError) as e:
        is_standard_email('testexamcom', ALLOWED)
    assert 'must contain 1= @ in the middle and \'.\' in the second part, after @ and at least one character after' == \
           e.value.args[0]


def test_email_validate5():
    with pytest.raises(ValueError) as e:
        is_standard_email('_es@texam.com', ALLOWED)
    assert 'must contain 1= @ in the middle and \'.\' in the second part, after @ and at least one character after' == \
           e.value.args[0]


def test_email_validate6():
    with pytest.raises(ValueError) as e:
        is_standard_email('test@exam.com_', ALLOWED)
    assert 'must contain 1= @ in the middle and \'.\' in the second part, after @ and at least one character after' == \
           e.value.args[0]


# ---------------------------------------------------------------------------------------------------------------------

def test_correct_chars_email_validate1():
    with pytest.raises(ValueError) as e:
        is_correct_chars_email('test@exam.com*', EMAIL_ALLOWED)
    assert 'Invalid email chars' == e.value.args[0]


def test_correct_chars_email_validate2():
    with pytest.raises(ValueError) as e:
        is_correct_chars_email('te+st@exam.com', EMAIL_ALLOWED)
    assert 'Invalid email chars' == e.value.args[0]


def test_correct_chars_email_validate3():
    with pytest.raises(ValueError) as e:
        is_correct_chars_email('te//st@exam.com', EMAIL_ALLOWED)
    assert 'Invalid email chars' == e.value.args[0]


def test_correct_chars_email_validate4():
    with pytest.raises(ValueError) as e:
        is_correct_chars_email('привет@exam.com', EMAIL_ALLOWED)
    assert 'Invalid email chars' == e.value.args[0]


# ---------------------------------------------------------------------------------------------------------------------

def test_correct_2unsuitable_chars_email_validate1():
    with pytest.raises(ValueError) as e:
        is_2unsuitable_chars_email('e__m@mm.ru')
    assert 'Invalid email chars, __ -- .. ' == e.value.args[0]


def test_correct_2unsuitable_chars_email_validate2():
    with pytest.raises(ValueError) as e:
        is_2unsuitable_chars_email('e--m@mm.ru')
    assert 'Invalid email chars, __ -- .. ' == e.value.args[0]


def test_correct_2unsuitable_chars_email_validate3():
    with pytest.raises(ValueError) as e:
        is_2unsuitable_chars_email('e..m@mm.ru')
    assert 'Invalid email chars, __ -- .. ' == e.value.args[0]


def test_correct_2unsuitable_chars_email_validate4():
    with pytest.raises(ValueError) as e:
        is_2unsuitable_chars_email('e_.-m@mm.ru')
    assert 'Invalid email chars, __ -- .. ' == e.value.args[0]


if __name__ == '__main__':
    pytest.main()
