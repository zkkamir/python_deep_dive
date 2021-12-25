from collections.abc import Sequence
from numbers import Integral


class BaseValidator:
    def __init__(self, type_, min_, max_):
        self.type_ = type_
        self.min_ = min_
        self.max_ = max_

    def __set_name__(self, cls, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise ValueError(
                f'{self.name} must be of type {self.type_.__name__}.')
        if issubclass(self.type_, Sequence):
            if self.min_ is not None and len(value) < self.min_:
                raise ValueError(
                    f'length of {self.name} must be at least {self.min_}.')
            elif self.max_ is not None and len(value) > self.max_:
                raise ValueError(
                    f'length of {self.name} must be less than {self.max_}.')
        else:
            if self.min_ is not None and value < self.min_:
                raise ValueError(
                    f'{self.name} must be at least {self.min_}.')
            if self.max_ is not None and value > self.max_:
                raise ValueError(
                    f'{self.name} must be less than {self.max_}.')
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner_cls):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.name, None)


class IntegerField(BaseValidator):
    def __init__(self, min_value=None, max_value=None):
        super().__init__(Integral, min_value, max_value)


class CharField(BaseValidator):
    def __init__(self, min_length=0, max_length=None):
        super().__init__(str, min_length, max_length)


class Person:
    name = CharField(1, 10)
    age = IntegerField(0, 200)


p1 = Person()

p1.name = 'Mamad'
p1.age = 2

try:
    p1.name = 10
except ValueError as ex:
    print(ex)
try:
    p1.name = ''
except ValueError as ex:
    print(ex)
try:
    p1.name = '12345678910'
except ValueError as ex:
    print(ex)
try:
    p1.age = '12s'
except ValueError as ex:
    print(ex)
try:
    p1.age = -1
except ValueError as ex:
    print(ex)
try:
    p1.age = 1000
except ValueError as ex:
    print(ex)
