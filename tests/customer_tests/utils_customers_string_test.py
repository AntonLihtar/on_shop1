from string import ascii_letters, digits
from unittest import TestCase, main

from entities.utils_customer import validate_all_string_checks

ALLOWED = ascii_letters + digits


class UtilsCustomersTest(TestCase):
    def test_plus(self):
        with self.assertRaises(ValueError) as e:
            validate_all_string_checks('Anto1*', ALLOWED)
        self.assertEqual(f'Invalid string "Anto1*". Only allowed: {ALLOWED}', e.exception.args[0])

    def test_string_validate(self):
        with self.assertRaises(ValueError):
            validate_all_string_checks('1nton', ALLOWED)

    def test_string_validate3(self):
        with self.assertRaises(ValueError):
            validate_all_string_checks('An.ton', ALLOWED)

    def test_string_validate4(self):
        with self.assertRaises(ValueError):
            validate_all_string_checks('An*on', ALLOWED)

    def test_string_validate5(self):
        with self.assertRaises(ValueError):
            validate_all_string_checks('Anton__', ALLOWED)

    def test_string_validate6(self):
        with self.assertRaises(ValueError):
            validate_all_string_checks('An', ALLOWED)

    def test_string_validate7(self):
        with self.assertRaises(ValueError):
            validate_all_string_checks('', ALLOWED)

    def test_string_validate8(self):
        with self.assertRaises(ValueError):
            validate_all_string_checks('An se', ALLOWED)

    def test_string_validate9(self):
        with self.assertRaises(ValueError):
            validate_all_string_checks('A*1', ALLOWED)

    def test_string_validate10(self):
        with self.assertRaises(ValueError):
            validate_all_string_checks('Антон', ALLOWED)

    def test_string_validate11(self):
        with self.assertRaises(ValueError):
            validate_all_string_checks('Пgh', ALLOWED)


if __name__ == '__main__':
    main()
