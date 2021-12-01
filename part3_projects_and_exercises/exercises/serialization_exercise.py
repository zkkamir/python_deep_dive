from datetime import date, datetime
from decimal import Decimal
import json


class Stock:
    def __init__(self, symbol, date, open_, high, low, close, volume):
        self.symbol = symbol
        self.date = date
        self.open_ = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def __repr__(self):
        return f'Stock({self.symbol}, {self.date}, {self.open_}, ' + \
               f'{self.high}, {self.low}, {self.close}, {self.volume})'


class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.volume = volume
        self.commission = commission

    def __repr__(self):
        return f'Trade({self.symbol}, {self.timestamp}, {self.order}, ' + \
               f'{self.price}, {self.volume}, {self.commission})'


activity = {
    'quotes': [
        Stock('TSLA', date(2018, 11, 22),
              Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), Decimal('338.19'), 365_607),
        Stock('AAPL', date(2018, 11, 22),
              Decimal('176.66'), Decimal('177.25'), Decimal('176.64'), Decimal('176.78'), 3_699_184),
        Stock('MSFT', date(2018, 11, 22),
              Decimal('103.25'), Decimal('103.48'), Decimal('103.07'), Decimal('103.11'), 4_493_689)
    ],
    'trades': [
        Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12),
              'buy', Decimal('338.25'), 100, Decimal('9.99')),
        Trade('AAPL', datetime(2018, 11, 22, 10, 30, 5),
              'sell', Decimal('177.01'), 20, Decimal('9.99'))
    ]
}


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, Stock):
            obj = dict(
                datatype='Stock',
                symbol=arg.symbol,
                date=arg.date,
                open_=arg.open_,
                high=arg.high,
                low=arg.low,
                close=arg.close,
                volume=arg.volume

            )
            return obj
        if isinstance(arg, Trade):
            obj = dict(
                datatype='Trade',
                symbol=arg.symbol,
                timestamp=arg.timestamp,
                order=arg.order,
                price=arg.price,
                volume=arg.volume,
                commission=arg.commission
            )
            return obj
        if isinstance(arg, datetime):
            obj = dict(
                datatype='datetime',
                year=arg.year,
                month=arg.month,
                day=arg.day,
                hour=arg.hour,
                minute=arg.minute,
                second=arg.second
            )
            return obj
        if isinstance(arg, date):
            obj = dict(
                datatype='date',
                year=arg.year,
                month=arg.month,
                day=arg.day
            )
            return obj
        if isinstance(arg, Decimal):
            obj = dict(
                datatype='Decimal',
                value=str(arg)
            )
            return obj
        else:
            return super().default(arg)


# print(json.dumps(activity, cls=CustomJSONEncoder, indent=2))
