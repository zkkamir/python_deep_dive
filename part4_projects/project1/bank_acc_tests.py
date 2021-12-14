from datetime import datetime, timedelta
import unittest

from bank_acc import Account, TimeZone


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestAccount(unittest.TestCase):
    def test_create_timezone(self):
        tz = TimeZone('ABC', -1, -30)
        self.assertEqual('ABC', tz.name)
        self.assertEqual(timedelta(hours=-1, minutes=-30), tz.offset)

    def test_timezones_equal(self):
        tz1 = TimeZone('ABC', 1, 30)
        tz2 = TimeZone('ABC', 1, 30)
        self.assertEqual(tz1, tz2)

    def test_timezones_not_equal(self):
        tz = TimeZone('ABC', -1, -30)

        test_timezones = (
            TimeZone('DEF', -1, -30),
            TimeZone('ABC', -1, 0),
            TimeZone('ABC', 1, -30),
        )
        for i, test_tz in enumerate(test_timezones):
            with self.subTest(test_name=f'Test #{i}'):
                self.assertNotEqual(tz, test_tz)

    def test_create_account(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = 100.00

        a = Account(account_number, first_name, last_name, tz, balance)

        self.assertEqual(account_number, a.account_number)
        self.assertEqual(first_name, a.first_name)
        self.assertEqual(last_name, a.last_name)
        self.assertEqual(first_name + ' ' + last_name, a.full_name)
        self.assertEqual(tz, a.timezone)
        self.assertEqual(balance, a.balance)


if __name__ == '__main__':
    run_tests(TestAccount)
