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

    def as_dict(self):
        return dict(symbol=self.symbol,
                    date=self.date,
                    open_=self.open_,
                    high=self.high,
                    low=self.low,
                    close=self.close,
                    volume=self.volume
                    )

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

    def as_dict(self):
        return dict(symbol=self.symbol,
                    timestamp=self.timestamp,
                    order=self.order,
                    price=self.price,
                    volume=self.volume,
                    commission=self.commission
                    )

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
    def default(self, obj):
        if isinstance(obj, Stock) or isinstance(obj, Trade):
            result = obj.as_dict()
            result['object'] = obj.__class__.__name__
            return result
        elif isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, Decimal):
            return str(obj)
        else:
            return super().default(obj)


# print(json.dumps(activity, cls=CustomJSONEncoder, indent=2))
