from string import ascii_letters, digits

"""
a module stores all the functions for a class Customer
"""

ALLOWED = ascii_letters + digits
EMAIL_ALLOWED = ascii_letters + digits + '.@_-'

"""
string checking --------------------------------
"""


def validate_string_ascii(value: str, allowed: str):
    if not all(n in allowed for n in value):
        raise ValueError(f'Invalid string "{value}". Only allowed: {ALLOWED}')


def validate_string_1char(value: str):
    if not value[:1].isalpha():
        raise ValueError(f'Invalid string "{value}". 1 character must be a letter')


def validate_len_string(value: str):
    if len(value) < 3:
        raise ValueError(f'Len {value} < 3')


def validate_all_string_checks(value: str, allowed: str):
    validate_string_ascii(value, allowed),
    validate_len_string(value),
    validate_string_1char(value)


"""
email checking --------------------------------
"""


def is_standard_email(value: str, allowed: str) -> bool:
    return all([value.count('@') == 1,
                '.' in value.split('@')[1][1:],  # dot in 2 parts after character
                value[:1] in allowed,
                value[-1:] in allowed])


def is_correct_chars_email(value: str, email_allowed: str) -> bool:
    return all(n in email_allowed for n in value)


def is_2unsuitable_chars_email(value: str) -> bool:
    """Function returns false if 2 characters together"""
    res = []
    for it in range(len(value) - 1):
        res.append(not (value[it] in '._-' and value[it + 1] in '._-'))
    return all(res)


def is_all_email_checks_valid(value: str, allowed: str, email_allowed) -> bool:
    return all([is_standard_email(value, allowed),
                is_correct_chars_email(value, email_allowed),
                is_2unsuitable_chars_email(value)])


"""
telephone checking --------------------------------
"""


def is_correct_telephone(value: str) -> bool:
    if len(value) == 12 and value[0] == '+' and value[1:].isdigit():
        return True
    elif len(value) == 11 and value.isdigit():
        return True
    else:
        return False


if __name__ == '__main__':
    assert validate_string_ascii('Anto1',ALLOWED) is True
    assert validate_all_string_checks('Anton', ALLOWED)
    assert validate_all_string_checks('Anto1', ALLOWED)
    assert validate_all_string_checks('1nton', ALLOWED)
    assert validate_all_string_checks('An.ton', ALLOWED)
    assert validate_all_string_checks('Anton.', ALLOWED)
    assert validate_all_string_checks('An*on', ALLOWED)
    assert validate_all_string_checks('*Anton', ALLOWED)
    assert validate_all_string_checks('Anton__', ALLOWED)
    assert validate_all_string_checks('An', ALLOWED)
    assert validate_all_string_checks('', ALLOWED)

    assert is_all_email_checks_valid('test@example.com', ALLOWED, EMAIL_ALLOWED) is True
    assert is_all_email_checks_valid('11@1.1', ALLOWED, EMAIL_ALLOWED) is True
    assert is_all_email_checks_valid('1-1@tyu.1', ALLOWED, EMAIL_ALLOWED) is True
    assert is_all_email_checks_valid('test@.com', ALLOWED, EMAIL_ALLOWED) is False
    assert is_all_email_checks_valid('tes.t@.com', ALLOWED, EMAIL_ALLOWED) is False
    assert is_all_email_checks_valid('test@example.co@m', ALLOWED, EMAIL_ALLOWED) is False
    assert is_all_email_checks_valid('t@est@example.com', ALLOWED, EMAIL_ALLOWED) is False
    assert is_all_email_checks_valid('testexample.co@m', ALLOWED, EMAIL_ALLOWED) is False
    assert is_all_email_checks_valid('11..@tr.1', ALLOWED, EMAIL_ALLOWED) is False
    assert is_all_email_checks_valid('11@1..1', ALLOWED, EMAIL_ALLOWED) is False
    assert is_all_email_checks_valid('1__1@1.ru', ALLOWED, EMAIL_ALLOWED) is False
    assert is_all_email_checks_valid('1--1@ru.1', ALLOWED, EMAIL_ALLOWED) is False
    assert is_all_email_checks_valid('_12rt@tyu.ru', ALLOWED, EMAIL_ALLOWED) is False
    assert is_all_email_checks_valid('.*12rt@tyu.ru', ALLOWED, EMAIL_ALLOWED) is False
    assert is_all_email_checks_valid('12rt@tyu.ru.', ALLOWED, EMAIL_ALLOWED) is False
    assert is_all_email_checks_valid('1_-2rt@tyu.ru', ALLOWED, EMAIL_ALLOWED) is False

    assert is_correct_telephone('+79231234567') is True
    assert is_correct_telephone('89231234567') is True
    assert is_correct_telephone('+792312345677') is False
    assert is_correct_telephone('+792312345') is False
    assert is_correct_telephone('*79231234567') is False
    assert is_correct_telephone('+7923123456r') is False
    assert is_correct_telephone('+79231II4567') is False
    assert is_correct_telephone('8923123456T') is False
    assert is_correct_telephone('+7923123456_') is False
    assert is_correct_telephone('_79231234567') is False
    assert is_correct_telephone('8_231234567') is False
