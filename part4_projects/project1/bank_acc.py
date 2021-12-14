from collections import namedtuple
from itertools import count
import numbers
from datetime import datetime, timedelta


# an easy-to-use object to parse confirmation codes to.
Confirmation = namedtuple(
    'Confirmation', 'account_number transaction_code transaction_id time_utc time')


class TimeZone:
    def __init__(self, name, hour_offset, minute_offset):
        if name is None or len(str(name).strip()) == 0:
            raise ValueError('Timezone name cannot be empty.')

        self._name = str(name).strip()

        if not isinstance(hour_offset, numbers.Integral):
            raise ValueError('Hour offset must be an integer.')

        if not isinstance(minute_offset, numbers.Integral):
            raise ValueError('Minute offset must be an integer.')
        if minute_offset > 59 or minute_offset < -59:
            raise ValueError(
                'Minutes offset must be between -59 and 59 (inclusive).')
        offset = timedelta(hours=hour_offset, minutes=minute_offset)
        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError('Offset must be between -12:00 an +14:00')

        self._offset_hours = hour_offset
        self._offset_minutes = minute_offset
        self._offset = offset

    @property
    def offset(self):
        return self._offset

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        return (isinstance(other, TimeZone) and
                self.name == other.name and
                self._offset_hours == other._offset_hours and
                self._offset_minutes == other._offset_minutes)

    def __repr__(self):
        return(f'TimeZone(name="{self.name}",'
               f'hour_offset={self._offset_hours},'
               f'minute_offset={self._offset_minutes})')


class Account:
    transaction_counter = count(0)
    _interest_rate = 0.5  # percent
    _transaction_codes = {
        'deposit': 'D',
        'withdraw': 'W',
        'interest': 'I',
        'rejected': 'X'
    }

    def __init__(self, account_number, first_name, last_name,
                 timezone=None, initial_balance=0):
        self._account_number = account_number
        self.first_name = first_name
        self.last_name = last_name

        if timezone is None:
            timezone = TimeZone('UTC', 0, 0)
        self.timezone = timezone

        self._balance = self.validate_real_number(initial_balance, 0)

    @property
    def account_number(self):
        return self._account_number

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self.validate_and_set_name('_first_name', value, 'First name')

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self.validate_and_set_name('_last_name', value, 'Last name')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def timezone(self):
        return self._timezone

    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError('Time Zone must be a valid TimeZone object.')
        self._timezone = value

    @property
    def balance(self):
        return self._balance

    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate

    @classmethod
    def set_interest_rate(cls, value):
        if not isinstance(value, numbers.Real):
            raise ValueError('Interest rate must be a real number.')
        if value < 0:
            raise ValueError('Interest rate cannot be negative.')
        cls._interest_rate = value

    @staticmethod
    def validate_real_number(value, min_value=None):
        if not isinstance(value, numbers.Real):
            raise ValueError('Value must be a real number.')

        if min_value is not None and value < min_value:
            raise ValueError(f'Value must be at least {min_value}.')

        return value

    def generate_conformation_code(self, transaction_code):
        dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return (f'{transaction_code}-{self.account_number}-{dt_str}-'
                f'{next(Account.transaction_counter)}')

    def validate_and_set_name(self, attr_name, name, field_title):
        if not name or len(str(name).strip()) == 0:
            raise ValueError(f'{field_title} cannot be empty')
        setattr(self, attr_name, name)

    @staticmethod
    def parse_confirmation_code(confirmation_code, preferred_time_zone=None):
        # dummy-A100-20211212114523-101
        parts = confirmation_code.split('-')
        if len(parts) != 4:
            raise ValueError('Invalid confirmation code')
        transaction_code, account_number, raw_dt_utc, transaction_id = parts

        try:
            dt_utc = datetime.strptime(raw_dt_utc, '%Y%m%d%H%M%S')
        except ValueError as ex:
            raise ValueError('Invalid transasaction datetime') from ex

        if preferred_time_zone is None:
            preferred_time_zone = TimeZone('UTC', 0, 0)

        if not isinstance(preferred_time_zone, TimeZone):
            raise ValueError('Invalid TimeZone specified.')

        dt_prefered = dt_utc + preferred_time_zone.offset
        dt_prefered_str = f'{dt_prefered.strftime("%Y-%m-%d %H:%M:%S")} {preferred_time_zone.name}'

        return Confirmation(account_number, transaction_code, transaction_id,
                            dt_utc.isoformat(), dt_prefered_str)

    def deposit(self, value):
        value = Account.validate_real_number(value, 0.01)
        transaction_code = Account._transaction_codes['deposit']
        conf_code = self.generate_conformation_code(transaction_code)
        self._balance += value
        return conf_code

    def withdraw(self, value):
        value = Account.validate_real_number(value, 0.01)
        accepted = False

        if self.balance - value < 0:
            # insufficient funds
            transaction_code = Account._transaction_codes['rejected']
        else:
            accepted = True
            transaction_code = Account._transaction_codes['withdraw']
        conf_code = self.generate_conformation_code(transaction_code)

        if accepted:
            self._balance -= value
        return conf_code

    def pay_interest(self):
        interest = self.balance * Account.get_interest_rate() / 100
        conf_code = self.generate_conformation_code(
            Account._transaction_codes['interest'])
        self._balance += interest
        return conf_code
