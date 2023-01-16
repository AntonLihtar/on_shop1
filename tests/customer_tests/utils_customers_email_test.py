from string import ascii_letters, digits
import pytest
from entities.utils_customer import is_all_email_checks_valid

ALLOWED = ascii_letters + digits
EMAIL_ALLOWED = ascii_letters + digits + '.@_-'


# assert is_all_email_checks_valid() is True

# assert is_all_email_checks_valid('1-1@tyu.1', ALLOWED, EMAIL_ALLOWED) is True
# assert is_all_email_checks_valid('test@.com', ALLOWED, EMAIL_ALLOWED) is False
# assert is_all_email_checks_valid('tes.t@.com', ALLOWED, EMAIL_ALLOWED) is False
# assert is_all_email_checks_valid('test@example.co@m', ALLOWED, EMAIL_ALLOWED) is False
# assert is_all_email_checks_valid('t@est@example.com', ALLOWED, EMAIL_ALLOWED) is False
# assert is_all_email_checks_valid('testexample.co@m', ALLOWED, EMAIL_ALLOWED) is False
# assert is_all_email_checks_valid('11..@tr.1', ALLOWED, EMAIL_ALLOWED) is False
# assert is_all_email_checks_valid('11@1..1', ALLOWED, EMAIL_ALLOWED) is False
# assert is_all_email_checks_valid('1__1@1.ru', ALLOWED, EMAIL_ALLOWED) is False
# assert is_all_email_checks_valid('1--1@ru.1', ALLOWED, EMAIL_ALLOWED) is False
# assert is_all_email_checks_valid('_12rt@tyu.ru', ALLOWED, EMAIL_ALLOWED) is False
# assert is_all_email_checks_valid('.*12rt@tyu.ru', ALLOWED, EMAIL_ALLOWED) is False
# assert is_all_email_checks_valid('12rt@tyu.ru.', ALLOWED, EMAIL_ALLOWED) is False
# assert is_all_email_checks_valid('1_-2rt@tyu.ru', ALLOWED, EMAIL_ALLOWED) is False

def test_valid_email():
    assert is_all_email_checks_valid('test@example.com', ALLOWED, EMAIL_ALLOWED)


def test_email_validate1():
    with pytest.raises(TypeError) as e:
        is_all_email_checks_valid('test@.com', ALLOWED, EMAIL_ALLOWED)
    assert 'can only concatenate str (not "int") to str' == e.value.args[0]


if __name__ == '__main__':
    pytest.main()
