from string import ascii_letters, digits
import utils_customer as u_c

"""
The module contains the Buyer class and its attributes
"""

ALLOWED = ascii_letters + digits
EMAIL_ALLOWED = ascii_letters + digits + '.@_-'
LEN_PASSWORD = 7  # min length password = 8


class Customer:

    def __init__(self, name, last_name, email, password, telephone, address):
        """All attributes == str"""
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.telephone = telephone
        self.address = address

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        u_c.validate_all_string_checks(name, ALLOWED)
        self._name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        u_c.validate_all_string_checks(last_name, ALLOWED)
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str):
        if u_c.is_all_email_checks_valid(email, ALLOWED, EMAIL_ALLOWED):
            self._email = email
        else:
            raise ValueError(f'Only allowed in email: {EMAIL_ALLOWED}')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password: str):
        if len(password) > LEN_PASSWORD:
            self._password = password
        else:
            raise ValueError(f'len password <= 8')

    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, telephone: str):
        if u_c.is_correct_telephone(telephone):
            self._telephone = telephone
        else:
            raise ValueError(f'telephone = wrong format : +79990004444 or 89990004444')

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address: str):
        u_c.validate_string_ascii(address, ALLOWED)
        u_c.validate_len_string(address)
        self._address = address


if __name__ == '__main__':
    customer = Customer('Victor', 'Sholc', '1pass@mail.com', 'pass12323', '+79315000321', 'Vologda')
    customer2 = Customer('Ful', 'Fu1i1ll', '2p_ass@mail.com', '*pass1***', '82293150000', 'o22')
