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


def is_standard_email(value: str, allowed: str):
    flag = True
    if value.count('@') == 1:
        flag = not all(['.' in value.split('@')[1][1:],  # dot in 2 parts after character
                        value[:1] in allowed,
                        value[-1:] in allowed])
    if flag:
        raise ValueError(
            f'must contain 1= @ in the middle and \'.\' in the second part, after @ and at least one character after')


def is_correct_chars_email(value: str, email_allowed: str):
    for n in value:
        if n not in email_allowed:
            raise ValueError('Invalid email chars')


def is_2unsuitable_chars_email(value: str):
    for it in range(len(value) - 1):
        if value[it] in '._-' and value[it + 1] in '._-':
            raise ValueError('Invalid email chars, __ -- .. ')


def is_all_email_checks_valid(value: str, allowed: str, email_allowed):
    is_standard_email(value, allowed)
    is_correct_chars_email(value, email_allowed)
    is_2unsuitable_chars_email(value)


"""
telephone checking --------------------------------
"""


def is_correct_telephone(value: str):
    if not any([len(value) == 12 and value[0] == '+' and value[1:].isdigit(),
                len(value) == 11 and value.isdigit()]):
        raise ValueError('Invalid number only allowed +79991112222 or 89991112222')


if __name__ == '__main__':
    is_correct_telephone('+79991231234')
