from numbers import Integral


class IntegerField:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, cls, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, Integral):
            raise ValueError(f'{self.name} must be an integral number.')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(
                f'{self.name} must be at least {self.min_value}.')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(
                f'{self.name} must be less than {self.max_value}.')
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner_cls):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.name, None)


class CharField:
    def __init__(self, min_length=0, max_length=None):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, cls, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.name} must be a string.')
        if len(value) < self.min_length:
            raise ValueError(
                f'{self.name} must be at least {self.min_length} characters long.')
        if self.max_length is not None and len(value) > self.max_length:
            raise ValueError(
                f'{self.name} must be shorter than {self.max_length} characters.')
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner_cls):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.name, None)


class Person:
    name = CharField(1, 50)
    age = IntegerField(0, 200)
